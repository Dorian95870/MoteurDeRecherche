package code;

import java.util.ArrayList;
import java.util.HashMap;

public class app {

	public static void main(String[] args) {
		
		//A few ways to use it:
		JsonExplorer explorer = new JsonExplorer("C:/Users/mathi/Downloads/dataset2.json");
		System.out.println(explorer.getFromIndex(70L));
		System.out.println(explorer.getFromIndex(70L).get("title"));
		System.out.println(explorer.getFromCateg("title"));
		
		HashMap<String, HashMap<Long, ArrayList<Integer>>> index = IndexGen.start(explorer.getFromCateg("title"));
		System.out.println(index);
	}
}
