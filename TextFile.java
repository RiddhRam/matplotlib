import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
/**
 * @author <Riddh Ramburuth 220388724>
 * This class implements an object that stores text contents loaded from a file.
 * It also contains methods that:
 * - return the text contents as a List of words
 * - compute the word and letter frequencies and return those as a Map
 */
public class TextFile {
	
	private String filename;
	private List<String> wordList = new ArrayList<>();
	
	//add a constructor which takes the file name as a parameter
	public TextFile(String filename) {
        this.filename = filename;
    }

	//add a method that returns a List where each item is a word from a file
	//a word is any sequence of one or more characters separated with spaces
	//or punctuation characters
	public List<String> getWords() {
		
		// Create file object
		File fileToRead = new File(filename);
		
		try {
			// Create scanner object to read file
			Scanner fileReader = new Scanner(fileToRead);
			
			// Read through each line, and add it to the wordList
			while (fileReader.hasNextLine()) {
				wordList.add(fileReader.next());
			}
			// error handling
		} catch (FileNotFoundException e) {
			System.out.println("Error when reading file.");
			e.printStackTrace();
		}
	
		return wordList;
	}

	
	//add a method that computes letter frequencies in the text file
	//it treats lowercase and upppercase characters as one character
	//the method returns a Map object of Character to Integer (characters are
	//uppercase letters
	public HashMap<Character, Integer> getLetterFrequencies() {
		
		// Create a HashMap
		// Key: Character, Value: Integer
		HashMap<Character, Integer> letterFrequencies = new HashMap<>();
		
		// Iterate through upper case alphabet and initialize a key value of 0 for each character
		for (char c = 'A'; c != 'Z'; c++) {
			letterFrequencies.put(c, 0);
		}
		
		// Iterate through the wordList from earlier
		for (String word : wordList) {
			// Make everything uppercase
			String currentWord = word.toUpperCase();
			
			// Iterate through each character in current word
			for (int i = 0; i != currentWord.length(); i++) {
				// Get the current character
				char currentChar = currentWord.charAt(i);
				
				// Get the key value of the character
				int currentCount = letterFrequencies.get(currentChar);
				
				// Increment the value by 1 and put it back
				letterFrequencies.put(currentChar, currentCount+1);
			}
		}
		
		return letterFrequencies;
	}

	//add a method that computes word frequencies in the text file
	//the method returns a Map object of String to Integer
	public HashMap<String, Integer> getWordFrequencies() {
		// Create HashMap
		// Key: String, Value: Integer
		HashMap<String, Integer> wordFrequencies = new HashMap<>();
		
		// Initialize a key value of 0 for each word in wordFrequencies
		for (String word : wordList) {
			wordFrequencies.put(word, 0);
		}
		
		// Iterate through wordList again
		for (String word : wordList) {
			// Get the key value of this word
			int currentCount = wordFrequencies.get(word);
			
			// Increment it by 1 and put it back
			wordFrequencies.put(word, currentCount+1);
		}
		
		return wordFrequencies;
	}
}
