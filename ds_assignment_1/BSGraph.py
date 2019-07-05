class BSGraph:
    ActMov=[]
    edges=[[],[]]
    
    def readActMovfile(self, inputfile):
        lines = ""
        with open(inputfile, encoding='utf8') as f:
            lines = f.read().strip()
        splitLines = lines.split("\n")
        
        for line in splitLines:
            print(line)
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
    
    def displayMoviesOfActor(self, actor):
        return 
    
    def displayActorsOfMovie(self,movie):
        return 
    
    def findMovieRelation(self, movA,movB): 
        return 
    
    def findMovieTransRelation(self, movA, movB):
        return
    
def main():
    bsGraph = BSGraph()
    bsGraph.readActMovfile("inputPS2.txt")
    bsGraph.displayActMov()
    
if __name__== "__main__":
    main()
    
    