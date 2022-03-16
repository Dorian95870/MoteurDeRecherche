package code;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Iterator;

import org.json.simple.JSONObject;
import org.json.simple.parser.*;


/**
 * Class allowing to use data coming from a local JSON file
 * @author RODRIGUES Mathieu
 * @version 1.0
 */

public class JsonExplorer {
	private JSONObject js;
	
	/**
	 * Constructor, create a JSONObject from a JSON file
	 * @param FILEPATH, Path corresponding to the JSON file
	 */
	public JsonExplorer(String FILEPATH) {
		Object ob = new Object();
		try {
			ob = new JSONParser().parse(new FileReader(FILEPATH));
		} catch (Exception e) {
			e.printStackTrace();
		}

	    this.js = (JSONObject) ob;
	}
	
	/**
	 * Getter for the data value
	 * @return js, a JSONObject corresponding to our data
	 */
	public JSONObject getJs() {
		return js;
	}
	
	/**
	 * Get values of a specific document
	 * @param id, a Long corresponding to the index of the desired document
	 * @return map, a HashMap
	 */
	public HashMap<String, Object> getFromIndex(Long id) {	    
	    HashMap<String, Object> map = new HashMap<String, Object>();
	    int index = 0;
	    JSONObject resId = (JSONObject) getJs().get("id");
	    for (int i = 0; i < resId.size(); i++) {
			if ((Long)resId.get(resId.keySet().toArray()[i]) == id) {
				index = i;
				break;
			}
		}
	    
	    for (int i = 0; i < js.size(); i++) {
	    	JSONObject categorie = (JSONObject) getJs().get(getJs().keySet().toArray()[i]);
	    	try {
	    		Object elem =  categorie.get(categorie.keySet().toArray()[index]);
	    		map.put((String) js.keySet().toArray()[i], elem);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	    return map;
	}
	
	/**
	 * Get values of a specific category
	 * @param categ, a String that correspond to the desired category
	 * @return map, a HashMap
	 */
	public HashMap<Long, Object> getFromCateg(String categ) {	    
	    HashMap<Long, Object> map = new HashMap<Long, Object>();
	    JSONObject resId = (JSONObject) getJs().get("id");
	    JSONObject resCateg = (JSONObject) getJs().get(categ);
    	try {
    		for (int i = 0; i < resCateg.size(); i++) {
				map.put((Long) resId.get(resId.keySet().toArray()[i]), resCateg.get(resCateg.keySet().toArray()[i]));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	    return map;
	}
}
