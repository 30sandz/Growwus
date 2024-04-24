<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
// Set API key
$api_key = "sk-proj-FlmUvRw2jhvFApKi79mVT3BlbkFJI1TFLa2exEJlF8th83s4";

// Initializing conversation messages with a system message
$messages = [
    ["role" => "system", "content" => "You are a kind helpful assistant."]
];

// Define the main function
function main() {
    // Display introduction text
    echo "Welcome to the ChatGPT conversation!\n";

    // Start conversation loop
    conversationLoop();
}

// Function to handle conversation loop
function conversationLoop() {
    global $api_key, $messages;

    // Infinite loop for conversation
    while (true) {
        // Get user input
        $message = readline("User: ");

        // Check if user input is not empty
        if (!empty($message)) {
            // Append user's message to conversation history
            $messages[] = ["role" => "user", "content" => $message];

            // Generate AI assistant's reply
            $chat = createChat($api_key, $messages);

            // Extract reply from chat
            $reply = $chat->choices[0]->message->content;

            // Display AI assistant's reply
            echo "ChatGPT: $reply\n";

            // Append AI assistant's reply to conversation history
            $messages[] = ["role" => "assistant", "content" => $reply];

            // Check if user wants to end the conversation
            if (strtolower($message) === "exit") {
                break;
            }
        }
    }
}

// Function to create chat with OpenAI API
function createChat($api_key, $messages) {
    // API endpoint URL
    $url = "https://api.openai.com/v1/engines/davinci/completions";

    // Data to be sent in the request
    $data = [
        "model" => "gpt-3.5-turbo",
        "messages" => $messages,
        "temperature" => 1.0,
        "top_p" => 0.6,
        "n" => 1,
        "stream" => true
    ];

    // Convert data to JSON format
    $data_json = json_encode($data);

    // Initialize cURL session
    $ch = curl_init($url);

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Content-Type: application/json",
        "Authorization: Bearer $api_key"
    ]);

    // Execute cURL request and get response
    $response = curl_exec($ch);

    // Close cURL session
    curl_close($ch);

    // Decode JSON response
    $chat = json_decode($response);

    // Return chat object
    return $chat;
}

// Run the main function
main();

?>
    
</body>
</html>