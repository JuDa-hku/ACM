#include "vector.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void VectorExpand(vector *v)
{
  //void* p;
  if(v->length==v->allocateLen){
    v->elemList=(char*)(realloc(v->elemList, v->elemSize*(v->length)+v->initialAllocation*v->elemSize));
  //  v->elemList = (char*)p;
  v->allocateLen += v->initialAllocation;
  }
  //bug here !!! 
}

void VectorNew(vector *v, int elemSize, VectorFreeFunction freeFn, int initialAllocation)
{
  assert(initialAllocation>=0);
  if(initialAllocation==0)
    initialAllocation=10;
  v->initialAllocation=initialAllocation;
  v->freeFn=freeFn;
  v->elemSize=elemSize;
  v->elemList=(char*)(malloc(v->elemSize*v->initialAllocation));
  v->length=0;
  v->allocateLen=v->initialAllocation;
}

void VectorDispose(vector *v)
{
  if(v->freeFn!=NULL){
    for(int i=v->length-1; i>=0;i--)
      v->freeFn(v->elemList+i*v->elemSize);
  }
  free(v->elemList);
}

int VectorLength(const vector *v)
{ 
return v->length;
 }

void *VectorNth(const vector *v, int position)
{ 
  assert(position>=0&&position<v->length);
  void * result = (void*)(v->elemList+position*v->elemSize);
  return result; 
}

void VectorReplace(vector *v, const void *elemAddr, int position)
{
  assert(position>=0);
  assert(position<=v->length);
  void* dest=v->elemList+position*v->elemSize;
  memcpy(dest, elemAddr, v->elemSize);
}

void VectorInsert(vector *v, const void *elemAddr, int position)
{
  VectorExpand(v);
  assert(position>=0&&position<=v->length);
  if(position==v->length)
    {
      VectorReplace(v, elemAddr, position);
      v->length+=1;
    }
  else
    {
      void* src=v->elemList+(position)*v->elemSize;
      void* dest=v->elemList+(position+1)*v->elemSize;
      memmove(dest, src, v->elemSize*(v->length-position));
      VectorReplace(v, elemAddr, position);
      v->length+=1;
    }
}

void VectorAppend(vector *v, const void *elemAddr)
{
  VectorExpand(v);
  memcpy(v->elemList+v->elemSize*v->length, elemAddr, v->elemSize);
   v->length += 1;
}

void VectorDelete(vector *v, int position)
{

    void* dest=v->elemList+position*v->elemSize;
    void* src=v->elemList+(position+1)*v->elemSize;
  memmove(dest, src, v->elemSize*(v->length-position-1));
  //  v->freeFn(v->elemList+(v->length-1)*v->elemSize);
  v->length-=1;
}

void VectorSort(vector *v, VectorCompareFunction compare)
{
  assert(compare != NULL);
  void *base = v->elemList;
  size_t nmemb=v->length;
  size_t size = v->elemSize;
  qsort(base, nmemb, size,compare);
}

void VectorMap(vector *v, VectorMapFunction mapFn, void *auxData)
{
  assert(mapFn!=NULL);
  void *base = v->elemList;
  for(int i=0; i<v->length; i++)
    mapFn((char*)base+i*v->elemSize, auxData);
}

static const int kNotFound = -1;
int VectorSearch(const vector *v, const void *key, VectorCompareFunction searchFn, int startIndex, bool isSorted)
{
  assert(startIndex>=0&&startIndex<=v->length);
  assert(key!=NULL);
  void* base= v->elemList+startIndex*v->elemSize;
  size_t nmemb = v->length-startIndex;
  if(isSorted)
    {
      void * tmp = bsearch(key, base,nmemb, v->elemSize,searchFn);
      if(tmp==NULL)
	return -1;
      int result=(int)((char*)tmp-(char*)base)/v->elemSize+startIndex;
      return result;
    }
  else
    {
      for(int i=startIndex; i<v->length; i++)
	if(searchFn((char*)base+(i-startIndex)*v->elemSize,key) == 0)
	  return i;
    }
  return -1;
} 
