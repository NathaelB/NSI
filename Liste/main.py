from typing import Union,TypeVar,Any
Liste = TypeVar('Liste')

class Liste:
   def __init__(self,val:Union[Liste,Any]=None,queue:Liste = None):

       """Instancie  un objet Liste """
       if type(val)==Liste:
           self.tete = val.tete
           self.queue = val.queue
       else:
           self.tete=val
           self.queue=queue

   def est_vide(self):
       """ Retourne True si la liste est vide et False dans le cas contraire"""
       return self.tete is None

   def add_head(self,valeur):
       """ajoute une <valeur> en début de liste"""
       l = Liste(valeur)
       l.queue = Liste(self)
       self.tete,self.queue = l.tete,l.queue


   def delete_head(self):
       """supprime une <valeur> en fin de liste"""
       self.tete = self.queue.tete
       self.queue = self.queue.queue


   def add_queue(self,val):
       """ajoute une <valeur> en fin de liste"""
       queue = self.queue
       tete = self.tete

       while type(queue) is Liste: #3ème cas
           tete = queue.tete
           queue = queue.queue
       if tete is None: #Si tete = None
           tete = val
       else: #Si tete = val et que queue = none
           queue = Liste(val)
           queue = queue.queue

       # if tete is None:
       #     tete = val
       # if queue is None:
       #     tete.queue = Liste(val)
       #     queue = queue.queue
       # else:
       #     queue = Liste(val)
       #     queue = queue.queue





   def __str__(self):
      """Retourne une chaîne de caractères des éléments de la Liste
      au format list python"""
      s="["
      tete = self.tete
      queue = self.queue
      while tete is not None:
          s+=str(tete)+","
          if queue is None:
              break
          tete = queue.tete
          queue = queue.queue
      s = s [0: -1]
      s+="]"
      return s

   def __len__(self):
       """Retourne le nombre d'élément de la liste"""
       if self.tete is None:
           return 0
       elif self.queue is None:
           return 1
       else:
           return 1 + self.queue.__len__()


def main():
    pass
if __name__ == '__main__':
    main()