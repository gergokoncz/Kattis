#include <stdio.h>

int main(){
	// start with scanning first graphsize
	// runs until graph size is -1
	int graph_size;
	int a = scanf("%d", &graph_size);
	while (graph_size != -1){
		int current_graph[graph_size][graph_size];
		// read graph
		for (int i = 0; i < graph_size; i++){
			for (int j = 0; j < graph_size; j++){
				int current_val;
				scanf("%d", &current_val);
				current_graph[i][j] = current_val;
			}
		}
		// build nn  
		for (int i = 0; i < graph_size; i++){
			//printf("starting for number %d\n", i);
			int nn[graph_size]; // neighbors of neighbors and zero it out
			for(int x = 0; x < graph_size; x++){
				nn[x] = 0;
			}
			for (int j = 0; j < graph_size; j++){
				if (current_graph[i][j] == 1){
					//printf("current graph is 1 for %d\n", j);
					for (int z = 0; z < graph_size; z++){
						if (current_graph[j][z] == 1){
							nn[z] = 1;
						}
					}
				}
			}
			int intriangle = 0;
			for (int b = 0; b < graph_size; b++){
				//printf("cg %d nn %d\t", current_graph[i][b],nn[b]);
				if (current_graph[i][b] == 1 & nn[b] == 1){
					intriangle = 1;
				}
			}
			if (intriangle == 0){
				printf("%d ", i);
			}
		}
		printf("\n");
		int a = scanf("%d", &graph_size);
	}
	return 0;
}
