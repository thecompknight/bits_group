class Node:
   
   def __init__(self,node_name):
       self.node_name = node_name

   def getNodeName(self):
       return self.node_name

class BSGraph:
   ActMov=[] # The list maintains the names of Movies and Actors

   # Two lists maintains the relationship between the Movies and the Actors
   # edges[0] holds the movie indices
   # edges[1] holds the Actov indices at the corresponding position to the edges[0]
   # for e.g., movie Index = 1 and Actor index1 = 2 and Actor Index2 = 3 (two actors / movie)
   #    then edges[0] = [1,1] and edges[1] = [2,3] 
   edges=[[],[]] 

   #--------Function addNode --------------------------------
   #This is a member function to add the Node to the Graph
   #The Node can contain either Movie Name or Actor Name.
   
   #~~~Runtime = O(1)~~~
   #---------------------------------------------------------
   def addNode(self,n):
      self.ActMov.append(n)

   #--------Function getNode --------------------------------
   #This function gets the Node present in the ActMov list
   #if not present returns None
      
   # ~~~Runtime = O(n)~~~
   #---------------------------------------------------------
   def getNode(self,name):
      for n in self.ActMov:
         if n.node_name == name:
            return n
      return None 

   #--------Function addEdge ----------------------------------------
   #creates the relationship between two nodes (here Movie and Actor)
   
   # ~~~Runtime = O(1)~~~
   #-----------------------------------------------------------------
   def addEdge(self,n1,n2):
      i1 = self.ActMov.index(n1)
      i2 = self.ActMov.index(n2)

      self.edges[0].append(i1)
      self.edges[1].append(i2)

   #--------Function readActMovfile--------------------------------------------------
   #Reads the input file and extracts the names of the Movies and Actors
   #builds the Graph and establishes the relationship between the Movies and Actors
   #Sample Input
   #Dangal / Aamir Khan / Fatima Sana
   #So it creates 3 Nodes for this line and uses the addNode to add the Nodes and
   #add addEdge to establish the relation ship

   #~~~ Runtime = O(n^2)
   #--------------------------------------------------------------------------------
   def readActMovfile(self,inputfile):
      lines = ""

      #open the input file. 
      with open(inputfile, encoding='utf8') as f:
            lines = f.read().strip()
            
      splitLines = lines.split("\n") #read all the lines into a list
        
      for line in splitLines: # iterate the lines
            movieWithActors = line.split("/") #tokenize with delimiter = '/'
               
            movieWithActors[0] = movieWithActors[0].strip() # get the movie token
            movieNode = self.getNode(movieWithActors[0]) # check if node is already present
            
            #if the node not found add it
            if movieNode == None: 
               self.addNode(Node(movieWithActors[0]))
               movieNode = self.getNode(movieWithActors[0])
            

            # there will be max 2 actor tokens
            
            for actor in movieWithActors[1:]:
                actor = actor.strip()
                actorNode = self.getNode(actor) # check if the actor already present
                if actorNode == None: # if the node is not found add it
                   self.addNode(Node(actor))
                   actorNode = self.getNode(actor)

                self.addEdge(movieNode,actorNode) #create the relation of the Actor with the Movie
                            
   #--------Function displayActMov-----------------------------------------------------
   # Displays all the Actors and Movies present in the given input file
   #
   # ~~~ Runtime = O(m+n) where m is the number of movies and n is the number of actors
   #------------------------------------------------------------------------------------
   def displayActMov(self):
                                    
        f= open("outputPS2.txt","a+") #open an output file to write to.
        f.write("--------Function displayActMov--------\n")
        
        #Get unique set of movie indexes
        movieSet = set(self.edges[0])
        f.write("Total no. of movies: "+str(len(movieSet))+"\n")
        
        #Get unique set of actor indexes
        actorSet = set(self.edges[1])
        f.write("Total no. of actors: "+str(len(actorSet))+"\n")
        f.write("\n")
        
        #If there are non-zero movies then there will be atleast one actor as well
        if len(movieSet)!=0:
            f.write("List of movies:\n")
            
            for movieIndex in movieSet:
                f.write(self.ActMov[movieIndex].getNodeName()+"\n")
            
            f.write("\n")
            f.write("List of actors:\n")
                
            for actorIndex in actorSet:
                f.write(self.ActMov[actorIndex].getNodeName()+"\n")
            
        f.write("-----------------------------------------\n")
        f.close()
   #--------Function getActorOrMovieAt -----------------------------------------------------
   # It is a helper function to return a particular Movie or Actor at a given index in the list
                            
   # ~~~~ Runtime = O(1) ~~~
   #----------------------------------------------------------------------------------------
   def getActorOrMovieAt(self,index):
        if index<0 or index >= len(self.ActMov): # check out of bounds
            return ""
        else:
            return self.ActMov[index].node_name
                            
   #--------Function getActorOrMovieIndex ---------------------------------------------------
   # It is a helper function to return an index particular Movie or Actor in the list
                            
   # ~~~ Runtime = O(1) ~~~
   #----------------------------------------------------------------------------------------                            
   def getActorOrMovieIndex(self, amNode):
        index = 0
        actorOrMovie = amNode.node_name.strip()
        for i in (self.ActMov):
            if i.node_name == actorOrMovie:
                return index #found
            index = index+1
        return -1 # not found
                            
   #--------Function displayActorsOfMovie ---------------------------------------------------
   # displays the list of Actors in a given Movie

   # ~~~ Runtime = O(n) ~~~
   #----------------------------------------------------------------------------------------                                                        
   def displayActorsOfMovie(self, movie):
        f= open("outputPS2.txt","a+")
        f.write("--------Function displayActorsOfMovie--------\n")
        f.write("Movie name: "+movie+"\n")
        f.write("List of Actors:\n")
        movie_index = self.getActorOrMovieIndex(self.getNode(movie))
        
        if movie_index != -1:
            index = 0
            for mi in self.edges[0]:
                if mi == movie_index: #movie index found in list of movies
                    ai = self.edges[1][index]
                    actor = self.getActorOrMovieAt(ai)
                    f.write(actor+"\n")
                index = index + 1
        else:
            f.write("Movie not found\n")
        f.close()
   #--------Function displayMoviesOfActor ---------------------------------------------------                        
   # displays the list of Movies of a given Actor
   #
   # ~~~ Runtime = O(n) ~~~
   #----------------------------------------------------------------------------------------                                                        
   def displayMoviesOfActor(self, actor):
        f= open("outputPS2.txt","a+")
        f.write("--------Function displayMoviesOfActor--------\n")
        f.write("Actor name: "+actor+"\n")
        f.write("List of Movies:\n")
        actor_index = self.getActorOrMovieIndex(self.getNode(actor))
        if actor_index != -1:
            index = 0
            for ai in self.edges[1]:
                if ai == actor_index: #actor index found in list of actors
                    mi = self.edges[0][index]
                    f.write(self.getActorOrMovieAt(mi)+"\n")
                index = index + 1
        else:
            f.write("Actor not found\n")
        f.close()
   #--------Function getActorsOfMovie --------------------------------------------
   # This is a helper function to return all the actors of a given movie
   #
   # ~~~ Runtime = O(n) ~~~
   #--------------------------------------------------------------------------------                           
   def getActorsOfMovie(self, movie):

        movie_index = self.getActorOrMovieIndex(self.getNode(movie))
        actors = []
        if movie_index != -1:
            index = 0
            for mi in self.edges[0]:
                if mi == movie_index: #movie index found in list of movies
                    ai = self.edges[1][index]
                    actor = self.getActorOrMovieAt(ai)
                    #print(actor)
                    actors.append(actor)
                index = index + 1
        return actors
   #--------Function getMovieRelation --------------------------------------------
   # This function finds out if there is an actor common to both the movies(input params)
   # if there exists a common actor then that is the relation.
   #
   # ~~~ Runtime = O(n^2) ~~~
   #--------------------------------------------------------------------------------         
   def getMovieRelation(self,movA,movB):
        actA = self.getActorsOfMovie(str(movA.strip()))
        actB = self.getActorsOfMovie(str(movB.strip()))
        for actorA in actA: # iterate actors of movie A
            for actorB in actB: # iterate actors of Movie B
                # compare if he/she same
                if actorA == actorB : #same actor
                    return actorA
                    
        return ""   # no common actor is both movies
                            
   #--------Function findMovieRelations --------------------------------------------
   # This is a helper function which reads the input string containing the relation
   #
   # ~~~ Runtime = O(n)
   #--------------------------------------------------------------------------------
    
   def findMovieRelations(self):
        lines = ""
        # open the input file
        with open("promptsPS2.txt", encoding='utf8') as fin:
            lines = fin.read().strip()
        splitLines = lines.split("\n") # read the lines to a list
        
        for line in splitLines:
            #check if the 'RMovies' string is present
            if "RMovies" in line:
                movies = line.split("RMovies:",1)[1]
                movies = movies.split(":")
                # find the relation between two tokens
                self.findMovieRelation(movies[0],movies[1])
        fin.close()
        
   #--------Function findMovieRelation --------------------------------------------
   # “Movie A is related to Movie B if there is at least one actor common in the
   # movies A and B. In this case, we write R(A, B)”.
   # e.g.,                             
   #Movie A: Dangal
   #Movie B: PK
   #Related: Yes, Aamir Khan (if no, display appropriate message)
   #
   # This function finds the common actor between two movies passed as input param
   #
   # ~~~ Runtime = O(1)
   #--------------------------------------------------------------------------------
    
   def findMovieRelation(self, movA,movB):
        
        f = open("outputPS2.txt","a+")
        
        f.write("--------Function findMovieRelation --------\n")
        f.write("Movie A: "+ movA+"\n")
        f.write("Movie B: "+ movB+"\n")
        actor = self.getMovieRelation(movA,movB)
        if (actor != ""):
            f.write("Related: Yes, "+ actor+"\n")
        else:
            f.write (" No Relation Found\n")
        f.close()
        return
   #--------Function findMovieTransRelations --------------------------------------------
   # This is a helper function which reads the input string containing the Trans relation
   #
   # ~~~ Runtime = O(n)
   #-------------------------------------------------------------------------------------
          
   def findMovieTransRelations(self):
        lines = ""
        with open("promptsPS2.txt", encoding='utf8') as fin:
            lines = fin.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #check if the 'TMovies' string is present
            
            if "TMovies" in line:
                movies = line.split("TMovies:",1)[1]
                movies = movies.split(":")
                
                self.findMovieTransRelation(movies[0],movies[1])
        fin.close()

   #--------Function findMovieTransRelation --------------------------------------------
   # Consider the following relation T on the movies. T(A, B) is true if
   # a. T(A, B) = R(A , B)
   #   (or)
   # b. There is a movie C such that R(A, C) and also R(C, B).
   #    Given any two movies A and B, verify if T(A, B) exists / is True?                            
   #
   # This function finds the common actor between two movies passed as input param or
   # the movies are related through another third movie by the any of the actors in
   # those movies
   #
   # ~~~ Runtime = O(n)
   #--------------------------------------------------------------------------------        
   def findMovieTransRelation(self, movA, movB):
        relation_found = False
        f = open("outputPS2.txt","a+")
        f.write("--------Function findMovieTransRelation --------\n")
        f.write("Movie A: "+ movA+"\n")
        f.write("Movie B: "+ movB+"\n")

       
        movA = movA.strip()
        movB = movB.strip()

        #check for case (a) where T(A,B) = R(A,B) 
        actor = self.getMovieRelation(movA,movB)
        if (actor != ""):
            f.write("Related: Yes, "+ movA + " > "+actor+" > " + movB + "\n")
            f.close()
            return
                            
        #check for the case (b) where T(A,B) = R(A,C) and R(C,B)
                            
        movieSet = set(self.edges[0])
        
        if len(movieSet)!=0:
            for movieIndex in movieSet:
                movC = self.ActMov[movieIndex].getNodeName()
                movC = movC.strip()
                if movC == movA : #skip the same movie
                    continue
                actor1 = self.getMovieRelation(movA,movC)
                            
                if actor1 !="": # there exists a R(A,C)
                    actor2 = self.getMovieRelation(movC,movB)
                    if actor2 != "": # there exists a R(C,B)
                        # Yes, MovA and MovB are T(A,B); print it as below format.
                        #Related: Yes, Dangal > Aamir Khan > PK > Anushka Sharma > ADHM
                        f.write("Related: Yes, "+movA+" > "+actor1+" > "+ movC + " > " + actor2 + " > " + movB + "\n")
                        relation_found = True
                            
        if not relation_found: # No relation found
            f.write("No Trans Relation found\n")
        f.close()
        return
                            
def main():
   bsGraph = BSGraph()
   bsGraph.readActMovfile("inputPS2.txt")
   bsGraph.displayActMov()
   bsGraph.displayActorsOfMovie("Dangal")
   bsGraph.displayMoviesOfActor("Aamir Khan")
   bsGraph.findMovieRelations()
   bsGraph.findMovieTransRelations()
                            
if __name__== "__main__":
    main()   
	

