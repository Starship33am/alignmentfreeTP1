from loading import load_directory
from kmers import enum_kmers, kmer2str
import time

def similarity(A, inter, B):
    return inter/A , inter/B

def jaccard(completeA, completeB, k):
  # Gets seq B and dico_A, outputs taille_I and taille_U
  
  #seqA=seqA[0]#[:30]
  #seqB=seqB[0]#[:30]
  dico={}
  taille_U=0
  taille_I=0

  for seqA in completeA:
    for kmer in enum_kmers(seqA,k):
      taille_U+=1
      if kmer not in dico:
        dico[kmer]=1
      else:
        dico[kmer]+=1

  for seqB in completeB:
    for kmer in enum_kmers(seqB,k):
      if kmer in dico:
        taille_I+=1
        dico[kmer]-=1
        if dico[kmer]==0:
          del dico[kmer]
      else:
        taille_U+=1
  return taille_I/taille_U, taille_I, taille_U

# La plus grande ressemblance entre 2 séquences est de 0.9377
# La plus petite ressemblance entre 2 séquences est de 0.001768

# Second method
def solution_heapq(file,k,s):
  # Creation des valeurs infini
  sketch = [float('-inf')]*s
  # Creation de lobjet heapq avec les valeurs infini
  heapq.heapify(sketch)

  # Pour tout les kmer, on garde les plus petites valeurs
  for seq in file:
    for kmer in enum_kmers(seq,k):
      # On cherche lelement le plus petit
      elem=sketch[0]
      # print('min',sketch[0])
      # print('complet', sketch)
      if -kmer>elem:
        # enlever min
        heapq.heappop(sketch)
        # ajout du nouvelle element
        heapq.heappush(sketch,-kmer)
        # print(kmer)
        # print(sketch)

  return sketch

def jaccard2(completeA, completeB):
  U=0
  I=0
  i=0
  j=0

  tailleA=len(completeA)
  tailleB=len(completeB)
  while i<tailleA and j<tailleB:
    if completeA[i]==completeB[j]:
      I+=1
      U+=1
      i+=1
      j+=1

    elif completeA[i]>completeB[j]:
      j+=1
      U+=1

    else:
      i+=1
      U+=1

  U+=(i-tailleA)+(j-tailleB)

  return (I/U), I, U


if __name__ == "__main__":
    # Load all the files in a dictionary
    data="/Users/brenda/Mi unidad (brenda.er.0203@gmail.com)/Sorbonne/Phyg/tme5_bren/data/"
    files = load_directory(data)
    k = 21
    letters = ['A', 'C', 'T', 'G']
    filenames = list(files.keys())
    distances=[]
    start_time = time.time()
    for i in range (len(files)):
        for j in range (i+1, len(files)):
            # --- Complete here ---
            #print(i,filenames[i])
            #print(j,filenames[j])
            distance_j, taille_I, taille_U = jaccard(files[filenames[i]], files[filenames[j]], k)
            sima,simb=similarity(len(files[filenames[i]][0]), taille_I, len(files[filenames[j]][0]))
            distances.append([i,j,distance_j,sima,simb])
            #print(filenames[i], filenames[j], j)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    # Second method
    k = 21
    s = 100
    distances=[]
    liste_sketch = []
    start_time = time.time()
    # Creation de tous les sketchs
    for i in range(len(files)):
        print(filenames[i])
        sketch = solution_heapq(files[filenames[i]],k,s)
        sketch=np.sort(-np.array(sketch))
        liste_sketch.append(sketch)

    for i in range (len(files)):
        for j in range (i+1, len(files)):
            # --- Complete here ---
            distance_j, taille_I, taille_U = jaccard2(liste_sketch[i], liste_sketch[j])
            distances.append([i,j,distance_j])

    end_time = time.time()
    print("Time : ", end_time-start_time)
