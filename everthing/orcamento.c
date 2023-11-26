//Orcamento de impressao 3d conforme horas de impressao e peso da peca


int main(){
int material[4];
int peso;
int horas;
int minutos;
int custo_hora;
int custo_grama;

int PLA = 110; //preco do material pla
material[0] = PLA/1000;

int ABS = 100; //preco do material abs
material[1] = ABS/1000;

int TPU = 140; //preco do material tpu
material[2] = ABS/1000;

int PETG = 120; //preco do material petg
material[3] = PETG/1000;


for(int i=0;i<4;i++) printf("%d", material[i]);

printf("Digite a quantidade de horas");
scanf("%d %d", &horas, &minutos);

}
