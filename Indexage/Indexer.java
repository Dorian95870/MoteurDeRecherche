import java.util.ArrayList;
import java.util.HashMap;

import org.json.simple.JSONObject;

public class Indexer {
	public static HashMap<String, HashMap<Long, ArrayList<Integer>>> start(HashMap<Long, Object> hashMap) {
		HashMap<String, HashMap<Long, ArrayList<Integer>>> data = new HashMap<String, HashMap<Long, ArrayList<Integer>>>();
		
		//Chaque documents
		for (int i = 0; i < hashMap.size(); i++) {
			HashMap<Long, ArrayList<Integer>> docs = new HashMap<Long, ArrayList<Integer>>();
			
			String title = ((String) hashMap.get(hashMap.keySet().toArray()[i])).toLowerCase();
			String[] words = title.split(" ");

			//Chaque mot
			for (int j = 0; j < words.length; j++) {
				ArrayList<Integer> tempPos = new ArrayList<Integer>();
				//Si le mot est déjà dans le doc
				if (docs.get(words[j]) != null) {
					tempPos = docs.get(words[j]);;
				}
				tempPos.add(j);
				
				if (data.get(words[j]) != null) {
					Long docId = (Long) hashMap.keySet().toArray()[i];
					data.get(words[j]).put(docId, tempPos);	
				}else {
					docs.put((Long) hashMap.keySet().toArray()[i], tempPos);
					data.put(words[j], docs);
				}
			}
		}
		return data;
	}
}
