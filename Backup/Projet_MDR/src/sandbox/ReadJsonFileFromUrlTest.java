package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.HashMap;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class ReadJsonFileFromUrlTest {
	  /**
	   * Read all the file char by char
	   * @param rd
	   * @return
	   * @throws IOException
	   */
	  private static String readAll(Reader rd) throws IOException {
		    StringBuilder sb = new StringBuilder();
		    int cp;
		    while ((cp = rd.read()) != -1) {
		    	sb.append((char) cp);
		    }
		    return sb.toString();
		  }
	  
	  	/**
	  	 * Read Json File From an URL
	  	 * @param url
	  	 * @return
	  	 * @throws IOException
	  	 * @throws JSONException
	  	 */
		public static JSONObject readJsonFromUrl(String url) throws IOException, JSONException {
		    InputStream is = new URL(url).openStream();
		    try {
		    	BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
		    	String jsonText = readAll(rd);
		    	JSONObject json = new JSONObject(jsonText);
		    	return json;
		    } 
		    finally {
		    	is.close();
		    }
		  }
		  
		  /**
		   * get the books on the json file
		   * @param json
		   * @return JSONArray with all the books as JSONObject
		   */
		  public static JSONArray getBooks(JSONObject json) { //but décomposer les results obtenus plus bas
			  JSONArray results = (JSONArray) json.get("results");
			  return results;
		  }
		  
		  /**
		   * Get books titles on the current JSON page
		   * @param jsonArray
		   * @return
		   */
		  public static HashMap<Integer,String> getBooksTitle(JSONArray jsonArray){
			  HashMap<Integer,String> books_IdTitleOnPage = new HashMap<Integer,String>();
			  for (int i = 0; i<jsonArray.length(); i++) {
				  int bookId = (int) ((JSONObject)jsonArray.get(i)).get("id");
				  String bookTitle = (String) ((JSONObject)jsonArray.get(i)).get("title");
				  books_IdTitleOnPage.put(bookId, bookTitle);
			  }
			  return books_IdTitleOnPage;
		  }
		  
		  /**
		   * Get all books Title on project gutenberg
		   * @param json
		   * @return HashMap(bookID,title)
		   * @throws JSONException
		   * @throws IOException
		   */
		  public static HashMap<Integer,String> getAllBooksTitle(JSONObject json) throws JSONException, IOException{
			  HashMap<Integer,String> books_IdTitle = new HashMap<Integer,String>();
			  JSONObject currentJsonPage = json;
			  while(!currentJsonPage.get("next").equals("null")) {
				  JSONArray booksOnPage = getBooks(currentJsonPage);
				  books_IdTitle = getBooksTitle(booksOnPage);
				  System.out.println(books_IdTitle.toString());
				  currentJsonPage = readJsonFromUrl(currentJsonPage.get("next").toString());
			  }
			return books_IdTitle;
		  }
		  
		  
		  /**
		   * Get all books Title on project gutenberg
		   * @param json
		   * @return ArrayList with all project gutenberg's books titles
		   * @throws JSONException
		   * @throws IOException
		   */
		  public static ArrayList<String> getAllBooksTitleInArray(JSONObject json) throws JSONException, IOException{
			  ArrayList<String> titles = new ArrayList<String>();
			  JSONObject currentJsonPage = json;
			  while(!currentJsonPage.get("next").equals("null")) {
				  JSONArray booksOnPage = getBooks(currentJsonPage);
				  for (int i = 0; i<booksOnPage.length(); i++) {
					  String bookTitle = (String) ((JSONObject)booksOnPage.get(i)).get("title");
					  titles.add(bookTitle);
				  }
				  System.out.println(titles.toString());
				  currentJsonPage = readJsonFromUrl(currentJsonPage.get("next").toString());
			  }
			return titles;
		  }
		  
		  public static void main(String[] args) throws IOException, JSONException {
			  JSONObject json = readJsonFromUrl("https://gutendex.com/books/");
			  //JSONArray booksOnPage = getBooks(json);
			  //HashMap<Integer,String> booksTitles = getBooksTitle(booksOnPage);
			  //HashMap<Integer,String> booksTitles = getAllBooksTitle(json);
			  ArrayList<String> titles = getAllBooksTitleInArray(json);
			  System.out.println(titles.toString());
			  //System.out.println(booksTitles.toString());
			  //System.out.println(((JSONObject)booksOnPage.get(0)).get("title"));
			  //System.out.println(json.get("results")); //trop grand pour être affiché 
			  //System.out.println(json.toString()); //trop grand pour être affiché
		    
		  }
}
