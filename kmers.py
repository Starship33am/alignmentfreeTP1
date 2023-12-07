def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11]) #mask binaire de 2 bit. 0b11 == 3
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


letters = ['A', 'C', 'T', 'G']
letters_map = {'A': 0, 'C': 1, 'T': 2, 'G': 3}


def enum_kmers(text,k):
  # Output: kmers containing only ACTG
  text = ''.join(filter(lambda base: base in letters, text)) #FILTRE get only ACTG
  mask  = (1<<(2*k))-1
  # Valeur du premier kmer
  pos=1
  kmer = 0
  kmerb = 0
  for i in text[:k]:
    nuc = letters_map[i]
    kmer<<= 2 # Decalage à gauche pour ajouter une nouvelle lettre
    kmer+= nuc # Ajouter le nouvel nucleotide au kmer
    ninvc=(nuc+2)&(0b11) # Trouver le nuc complementaire
    ninvc<<= 2*pos # Décalage du nouveau nucleotide pour l'ajouter au debut reverse comp
    kmerb+= ninvc # On ajoute le nouveau nucleotide au reste de rev comp
    pos+=1
  yield min(kmer,kmerb) # OUTPUT KMER

  # Valeurs des prochains kmer
  dec=2*k # decalage pour kmer inverse complementaire
  for i in text[k:]:
    nuc = letters_map[i]
    kmer<<= 2
    kmer+= nuc
    kmer&= mask

    ninvc=(nuc+2)&(0b11)
    ninvc<<= dec # On décale le nouveau nucleotide de k places pour l'ajouter au début
    kmerb+= ninvc # On ajoute le nouveau nucleotide au reste
    kmerb>>=2
    yield min(kmer,kmerb)
