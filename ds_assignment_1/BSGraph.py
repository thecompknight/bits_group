class BSGraph:
    ActMov=[]
    edges=[[],[]]
    
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
                    f.write(self.getActorOrMovieAt(ai)+"\n")
                index = index + 1
        else:
            f.write("Movie not found\n")
        f.close()
            
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
          
    def findMovieRelation(self, movA,movB): 
        return 
    
    def findMovieTransRelation(self, movA, movB):
        return
    
def main():
    bsGraph = BSGraph()
    bsGraph.readActMovfile("inputPS2.txt")
    #bsGraph.displayActMov()
    bsGraph.displayMoviesOfActors()
    bsGraph.displayActorsOfMovies()
    #bsGraph.displayMoviesOfActor("Aamir Khan")
    #bsGraph.displayMoviesOfActor("Randeep Hooda")
    
if __name__== "__main__":
    main()
    
    
