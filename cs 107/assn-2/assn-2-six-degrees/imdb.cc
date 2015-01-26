using namespace std;
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include "imdb.h"

const char *const imdb::kActorFileName = "actordata";
const char *const imdb::kMovieFileName = "moviedata";

imdb::imdb(const string& directory)
{
  const string actorFileName = directory + "/" + kActorFileName;
  const string movieFileName = directory + "/" + kMovieFileName;
  
  actorFile = acquireFileMap(actorFileName, actorInfo);
  movieFile = acquireFileMap(movieFileName, movieInfo);
}

bool imdb::good() const
{
  return !( (actorInfo.fd == -1) || 
	    (movieInfo.fd == -1) ); 
}

// you should be implementing these two methods right here... 
struct keyStr{
  const void* base;
  const char* data;
};

int comFunc(const void* a, const void* b){
  keyStr* key = (keyStr*) a;
  void* actorRecord = (char*)key->base+*(int*)b;
  char* actorName = (char*)actorRecord;
  char* string_key = (char*) key->data;
  return strcmp(string_key, actorName);
}


bool imdb::getCredits(const string& player, vector<film>& films) const {
  keyStr key_struct;
  key_struct.data=player.c_str();
  key_struct.base=actorFile;
  void* found;
  found=bsearch(&key_struct, (char*)actorFile+sizeof(int), *(int*)actorFile, sizeof(int), comFunc);
  
  if(found==NULL)
    return false; 

  short filmsLength;
  void* actorRecord=(char*)actorFile+*(int*)found;
  char* actorName=(char*) actorRecord;
  int buffer = strlen(actorName)+1;
  buffer += buffer%2;
  memcpy(&filmsLength, actorName+buffer, sizeof(short));
  int movieBuffer=buffer+sizeof(short);
  movieBuffer+= movieBuffer%4;

  for(int i=0; i<filmsLength; i++)
    {
      film tmpFilm;
      int movieOffset;
      memcpy(&movieOffset, actorName+movieBuffer+i*sizeof(int), sizeof(int));
      char* movieName=(char*)movieFile+movieOffset;
      int movieYear=1900+*((char*)movieFile+movieOffset+strlen(movieName)+1);
      tmpFilm.title=std::string(movieName);
      tmpFilm.year=movieYear;
      films.push_back(tmpFilm);
    }
  return true;
}


struct keyStr1{
  const void* base;
  const film* data;
};

int comFunc1(const void* a, const void* b){
  keyStr1* key = (keyStr1*) a;
  film movieRecord;
  char* movieTitle;
  movieTitle =(char*)((char*)key->base+*(int*)b);
  movieRecord.title=std::string(movieTitle);
  int buffer=strlen(movieTitle)+1;
  // std::cout<<"title:"<<movieRecord.title<<std::endl;
 movieRecord.year=1900+*((char*)key->base+*(int*)b+buffer);
 //  std::cout<<"year:"<<movieRecord.year<<std::endl;
  film movieRecord_key = *(film*)key->data;
  int result1=int(movieRecord_key<movieRecord);
  if(movieRecord_key==movieRecord)
    return 0;
  if(result1)
    return -1;
  else
    return 1;
}

bool imdb::getCast(const film& movie, vector<string>& players) const { 
  keyStr1 key;
  key.data=&movie;
  key.base=movieFile;
  int* found=(int*)(bsearch(&key,(char*)movieFile+sizeof(int), *(int*)movieFile, sizeof(int), comFunc1));
  if (found==NULL)
    return false; 
  void* movieBase=(char*)movieFile+*found;
  int Buffer=strlen((char*)movieBase)+1;
  int yearBuffer=Buffer+1;
  yearBuffer = yearBuffer+yearBuffer%2;
  short actorNum;
  memcpy(&actorNum, (char*)movieBase+yearBuffer, sizeof(short));
  int actorBuffer = yearBuffer+sizeof(short);
  actorBuffer=actorBuffer+actorBuffer%4;
  for(int i=0; i<actorNum; i++)
    {
      char* tmp;
      int actorIndex;
      memcpy(&actorIndex, (char*)movieBase+actorBuffer+i*sizeof(int), sizeof(int));
      tmp=(char*)actorFile+actorIndex;
	players.push_back(tmp);
    }
  return true;
}

imdb::~imdb()
{
  releaseFileMap(actorInfo);
  releaseFileMap(movieInfo);
}

// ignore everything below... it's all UNIXy stuff in place to make a file look like
// an array of bytes in RAM.. 
const void *imdb::acquireFileMap(const string& fileName, struct fileInfo& info)
{
  struct stat stats;
  stat(fileName.c_str(), &stats);
  info.fileSize = stats.st_size;
  info.fd = open(fileName.c_str(), O_RDONLY);
  return info.fileMap = mmap(0, info.fileSize, PROT_READ, MAP_SHARED, info.fd, 0);
}

void imdb::releaseFileMap(struct fileInfo& info)
{
  if (info.fileMap != NULL) munmap((char *) info.fileMap, info.fileSize);
  if (info.fd != -1) close(info.fd);
}
