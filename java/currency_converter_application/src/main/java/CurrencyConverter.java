import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;
import io.github.cdimascio.dotenv.Dotenv;

public class CurrencyConverter {
    private static Dotenv dotenv;
    private static String apiKey;
    private static String API_BASE_URL;

    static{
        dotenv = Dotenv.load();
        apiKey = dotenv.get("API_KEY");
        API_BASE_URL = "http://api.exchangeratesapi.io/v1/latest?access_key="+ apiKey; // from basic subscription we can only convert currency from EUR to other currencies.
        // API_BASE_URL = "http://api.exchangeratesapi.io/v1/convert?access_key="+ apiKey;
    }

    public static void main(String[] args) {


        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Enter the amount to convert: ");
            double amount = Double.parseDouble(reader.readLine());

            System.out.print("Enter the currency code to convert from (e.g., USD, EUR, GBP): ");
            String fromCurrency = reader.readLine().toUpperCase();

            System.out.print("Enter the currency code to convert to (e.g., USD, EUR, GBP): ");
            String toCurrency = reader.readLine().toUpperCase();

            double convertedAmount = convertCurrency(amount, fromCurrency, toCurrency);
            System.out.printf("%.2f %s is equal to %.2f %s\n", amount, fromCurrency, convertedAmount, toCurrency);

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static double convertCurrency(double amount, String fromCurrency, String toCurrency) throws IOException {
        String apiUrl = API_BASE_URL + "&base=" + fromCurrency + "&symbols=" + toCurrency;
        // This is applicable for all currency conversions
        // String apiUrl = API_BASE_URL + "&from=" + fromCurrency + "&to=" + toCurrency + "&amount=" + amount; 
        URL url = new URL(apiUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Accept", "application/json");

        if (conn.getResponseCode() != 200) {
            BufferedReader errorReader = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = errorReader.readLine()) != null) {
                response.append(inputLine);
            }
            errorReader.close();
            System.out.println("Error response: " + response.toString());
            throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
        }
        
        BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
        String response = br.readLine();
        conn.disconnect();

        JSONObject json = new JSONObject(response);
        JSONObject rates = json.getJSONObject("rates");
        double rate = rates.getDouble(toCurrency);

        return amount * rate;
    }
}