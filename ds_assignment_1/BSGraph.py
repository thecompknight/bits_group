class BSGraph:
    ActMov=[]
    edges=[[],[]]
    
    # The runtime complexity is O(m+n)^2 where m is the number of movies and n is the number of actors
    def readActMovfile(self, inputfile):
        lines = ""
        with open(inputfile, encoding='utf8') as f:
            lines = f.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #print(line)
            movieWithActors = line.split("/")
            
            #assume the movie doesnt exist to begin with
            movieIndex = len(self.ActMov)
            
            movieWithActors[0] = movieWithActors[0].strip()
            #if the movie is present already then update the movie index
            if movieWithActors[0] in self.ActMov:
                movieIndex = self.ActMov.index(movieWithActors[0])
            else:
                self.ActMov.append(movieWithActors[0])
                
            for actor in movieWithActors[1:]:
                
                actor = actor.strip()
                #assume actor doesnt exist to begin with
                actorIndex = len(self.ActMov)
                
                #if the actor is present already then update the actor index
                if actor in self.ActMov:
                    actorIndex = self.ActMov.index(actor)
                else:
                    self.ActMov.append(actor)

                #Now that we have the right indexes in the variables, create the edge                    
                self.edges[0].append(movieIndex)
                self.edges[1].append(actorIndex)

        #print(self.ActMov)
        #print(self.edges[0])
        #print(self.edges[1])

        #RMovies: Dangal : PK
        #RMovies: Kesari : Highway
        #--------Function findMovieRelation --------
        #Movie A: Dangal
        #Movie B: PK
        #Related: Yes, Aamir Khan (if no, display appropriate message)
        #-----------------------------------------
    
    def findMovieRelations(self):
        lines = ""
        with open("promptsPS2.txt", encoding='utf8') as fin:
            lines = fin.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #check if the 'searchActor' string is present
            if "RMovies" in line:
                movies = line.split("RMovies:",1)[1]
                movies = movies.split(":")
                #print(movies,movies[0].strip(),movies[1].strip())
                self.findMovieRelation(movies[0],movies[1])
        fin.close()
    
    #The runtime complexity of this function is O(m+n) where m is the number of movies and n is the number of actors
    def displayActMov(self):
        f= open("outputPS2.txt","a+")
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
                f.write(self.ActMov[movieIndex]+"\n")
            
            f.write("\n")
            f.write("List of actors:\n")
                
            for actorIndex in actorSet:
                f.write(self.ActMov[actorIndex]+"\n")
            
        f.write("-----------------------------------------\n")
        f.close()
        
    def getActorOrMovieAt(self,index):
        if index<0 or index >= len(self.ActMov):
            return ""
        else:
            return self.ActMov[index]
        
    def getActorOrMovieIndex(self, actorOrMovie):
        index = 0
        for i in (self.ActMov):
            if i == actorOrMovie:
                return index #found
            index = index+1
        return -1 # not found

    def displayActorsOfMovie(self, movie):
        f= open("outputPS2.txt","a+")
        f.write("--------Function displayActorsOfMovie--------\n")
        f.write("Movie name: "+movie+"\n")
        f.write("List of Actors:\n")
        movie_index = self.getActorOrMovieIndex(movie)
        
        if movie_index != -1:
            index = 0
            for mi in self.edges[0]:
                if mi == movie_index: #movie index found in list of movies
                    ai = self.edges[1][index]
                    actor = self.getActorOrMovieAt(ai)
                    #print(actor)
                    f.write(actor+"\n")
                index = index + 1
        else:
            f.write("Movie not found\n")
        f.close()
        
    def getActorsOfMovie(self, movie):

        movie_index = self.getActorOrMovieIndex(movie)
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
    
    def getActorsOfMovie2(self, movie):
    
        actors = []
        print ("looking for actors of movie : " + movie)
        movie_index = self.getActorOrMovieIndex(movie)
        print("movie index ="+ str(movie_index))
        if movie_index != -1:
            print("valid movie index")
            index = 0
            for mi in self.edges[0]:
                if mi == movie_index: #movie index found in list of movies
                    print("movie index found at " + str(mi))
                    ai = self.edges[1][index]
                    print("corresponding actor index = " + str(ai))
                    actor = self.getActorOrMovieAt(ai)
                    
                    print("Found : " +actor)
                    actors.append(actor)
                    index = index + 1
        return actors
    
    def displayMoviesOfActor(self, actor):
        f= open("outputPS2.txt","a+")
        f.write("--------Function displayMoviesOfActor--------\n")
        f.write("Actor name: "+actor+"\n")
        f.write("List of Movies:\n")
        actor_index = self.getActorOrMovieIndex(actor)
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
        
    def displayMoviesOfActors(self):
        lines = ""
        with open("promptsPS2.txt", encoding='utf8') as f:
            lines = f.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #check if the 'searchActor' string is present
            if "searchActor" in line:
                actor = line.split("searchActor:",1)[1]
                self.displayMoviesOfActor(actor)
        f.close()
                 
    def displayActorsOfMovies(self):
        lines = ""
        with open("promptsPS2.txt", encoding='utf8') as f:
            lines = f.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #check if the 'searchMovie' string is present
            if "searchMovie" in line:
                movie = line.split("searchMovie:",1)[1]
                self.displayActorsOfMovie(movie)
        f.close()
        
    def getMovieRelation(self,movA,movB):
        actA = self.getActorsOfMovie(str(movA.strip()))
        actB = self.getActorsOfMovie(str(movB.strip()))
        for actorA in actA:
            for actorB in actB:
                if actorA == actorB : #same actor
                    return actorA
                    
        return ""
    
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
    
    def findMovieTransRelations(self):
        lines = ""
        with open("promptsPS2.txt", encoding='utf8') as fin:
            lines = fin.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            #check if the 'searchActor' string is present
            
            if "TMovies" in line:
                movies = line.split("TMovies:",1)[1]
                movies = movies.split(":")
                
                self.findMovieTransRelation(movies[0],movies[1])
        fin.close()
        
    def findMovieTransRelation(self, movA, movB):
        relation_found = False
        f = open("outputPS2.txt","a+")
        f.write("--------Function findMovieTransRelation --------\n")
        f.write("Movie A: "+ movA+"\n")
        f.write("Movie B: "+ movB+"\n")

        movA.strip()
        movB.strip()
        movieSet = set(self.edges[0])
        #If there are non-zero movies then there will be atleast one actor as well
        if len(movieSet)!=0:
            for movieIndex in movieSet:
                movC = self.ActMov[movieIndex]
                movC.strip()
                if movC in movA :
                    continue
                actor1 = self.getMovieRelation(movA,movC)
                if actor1 !="":
                    actor2 = self.getMovieRelation(movC,movB)
                    if actor2 != "":
                        #Related: Yes, Dangal > Aamir Khan > PK > Anushka Sharma > ADHM
                        f.write("Related: Yes, "+movA+" > "+actor1+" > "+ movC + " > " + actor2 + " > " + movB + "\n")
                        relation_found = True
        if not relation_found:
            f.write("No Trans Relation found\n")
        f.close()
        return
    
def main():
    bsGraph = BSGraph()
    bsGraph.readActMovfile("inputPS2.txt")
    bsGraph.displayActMov()
    bsGraph.displayMoviesOfActors()
    bsGraph.displayActorsOfMovies()
    bsGraph.displayMoviesOfActor("Aamir Khan")
    bsGraph.displayMoviesOfActor("Randeep Hooda")
    bsGraph.findMovieRelations()
    bsGraph.findMovieTransRelations()
    
if __name__== "__main__":
    main()
    
    
