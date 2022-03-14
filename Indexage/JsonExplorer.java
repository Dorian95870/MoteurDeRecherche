import java.io.FileReader;
import java.util.HashMap;
import java.util.Iterator;

import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class JsonExplorer {
	private JSONObject js;
	
	public JsonExplorer(String FILEPATH) {
		Object ob = new Object();
		try {
			ob = new JSONParser().parse(new FileReader(FILEPATH));
		} catch (Exception e) {
			e.printStackTrace();
		}

	    this.js = (JSONObject) ob;
	}
	
	public JSONObject getJs() {
		return js;
	}

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
