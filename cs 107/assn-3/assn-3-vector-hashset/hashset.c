#include "hashset.h"
#include <assert.h>
#include <stdlib.h>
#include <string.h>


void HashSetNew(hashset *h, int elemSize, int numBuckets,
		HashSetHashFunction hashfn, HashSetCompareFunction comparefn, HashSetFreeFunction freefn)
{
  h->elemSize=elemSize;
  h->numBuckets=numBuckets;
  h->hashfn=hashfn;
  h->comparefn=comparefn;
  h->freefn=freefn;
  h->buckets=malloc(numBuckets*sizeof(vector));
  h->count=0;
  for(int i=0; i<numBuckets; i++)
    {
      VectorNew(h->buckets+i, elemSize, freefn, 4);
    }
}

void HashSetDispose(hashset *h)
{
  if(h->freefn!=NULL){
    for(int i=0; i<h->numBuckets; i++)
      VectorDispose(h->buckets+i);
  }
  free(h->buckets);
}

int HashSetCount(const hashset *h)
{ return h->count; }

void HashSetMap(hashset *h, HashSetMapFunction mapfn, void *auxData)
{
  assert(mapfn!=NULL);
  for(int i=0; i<h->numBuckets; i++)
    {
      VectorMap((h->buckets+i), mapfn, auxData);
    }
}

static vector *HashSetElemVector(const hashset *h, const void*elemAddr)
{
  int bucket = h->hashfn(elemAddr, h->numBuckets);
  return h->buckets+bucket;
}
   

void HashSetEnter(hashset *h, const void *elemAddr)
{
  assert(elemAddr!=NULL);
  void *find=HashSetLookup(h, elemAddr);
  if(find)
    {
      memcpy(find, elemAddr, h->elemSize);
    }
  else
    {
      vector* v=HashSetElemVector(h, elemAddr);
      VectorAppend(v, elemAddr);
      h->count++;
    }
}



void *HashSetLookup(const hashset *h, const void *elemAddr)
{
  vector *v = HashSetElemVector(h, elemAddr);
  int pos=VectorSearch(v, elemAddr, h->comparefn, 0, false);
  return pos==-1?NULL:VectorNth(v, pos);
}
