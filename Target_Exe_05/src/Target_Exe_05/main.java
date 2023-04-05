package Target_Exe_05;

public class main {

	public static void main(String[] args) {
		String str = "Target_Exe_05";
	    char[] ch = str.toCharArray();
	    
	    int start = 0;
		int fim = ch.length-1;
	    char apoio;

		System.out.println(str);
		while(fim>start){
	        apoio = ch[start];
	        ch[start] = ch[fim];
		    ch[fim] = apoio;
		    fim--;
		    start++;
	    }
		str = new String(ch);
		System.out.println(str);
	}

}
