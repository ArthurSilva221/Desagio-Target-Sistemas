package Target_Exe_04;

import java.util.HashMap;
import java.util.Map;

public class main {
	public static void main(String[] args) {
		 Map<String, Double> estado = new HashMap<>();
		 
		 double total = 0;
		 
		 estado.put("SP", (double) 67836.43);
		 estado.put("MG", (double) 36678.66);
		 estado.put("RJ", (double) 29229.88);
		 estado.put("ES", (double) 27165.48);
		 estado.put("OUTROS", (double) 19849.53);
		 
		 for(int x = 0; x < 5; x++) {
			 total = total + estado.get(Ler_Estado(x));
		 }
		 
		 System.out.printf("Faturamento total de todos os estados é R$%.2f %n", total);
		 System.out.printf("");
		 
		 for(int z=0;z<5;z++) {
			 String stad = Ler_Estado(z);
			 System.out.printf(stad);
			 System.out.printf(" Possui %.2f %n",(estado.get(Ler_Estado(z))*100)/total);
		 }
	}
	
	public static String Ler_Estado(Integer Estado) {
		  switch(Estado) {
		  	case 0:
		  		return "SP";
		  	case 1:
		  		return "MG";
		  	case 2:
		  		return "RJ";
		  	case 3:
		  		return "ES";
		  	case 4:
		  		return "OUTROS";
		  }
		return null;	  
	}

}
