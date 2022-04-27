package code;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * Class allowing the creation of the index
 * @author RODRIGUES Mathieu
 * @version 1.1
 */
public class IndexGen {

	/**
	 * Convert data to index
	 * @param in, a HashMap containing data to index
	 * @return res, a HashMap
	 */
	public static HashMap<String, HashMap<Long, ArrayList<Integer>>> start(HashMap<Long, Object> in) {
		//all data
		HashMap<String, HashMap<Long, ArrayList<Integer>>> res = 
		new HashMap<String, HashMap<Long, ArrayList<Integer>>>();
		for (int x = 0; x < in.size(); x++) {
			
			//doc
			Long docId = (Long) in.keySet().toArray()[x];
			String title = ((String) in.get(docId));
			String[] words = splitWords(title);
			HashMap<String, ArrayList<Integer>> positions = new HashMap<String, ArrayList<Integer>>();
			for (int y = 0; y < words.length; y++) {
				
				//word
				String word = words[y];
				ArrayList<Integer> wordPositions = positions.get(word);
				if (wordPositions == null) {
					wordPositions = new ArrayList<Integer>();
				}
				wordPositions.add(y);
				positions.put(word, wordPositions);
				HashMap<Long, ArrayList<Integer>> docData = res.get(word);
				if (docData == null) {
					docData = new HashMap<Long, ArrayList<Integer>>();
				}
				docData.put(docId, positions.get(word));
				res.put(word, docData);
			}
		}
		return res;
	}
	
	/**
	 * Separates a sentence into word lists
	 * @param in, the sentence to split
	 * @return a String[]
	 */
	private static String[] splitWords(String in) {
		return in.toLowerCase().split(" ");
	}
}