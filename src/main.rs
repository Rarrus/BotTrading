use request::blocking::Client;
use serde_json::Value;

fn main() {
    let client = Client::new();
    let response = client.get("https://api.example.com").send().unwrap();
    let json: Value = response.json().unwrap();
    
    // Process the JSON response here
    
    println!("{:?}", json);
}
