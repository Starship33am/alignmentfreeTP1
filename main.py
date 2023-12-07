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
