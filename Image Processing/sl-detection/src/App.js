// Import necessary libraries
import React, { Component } from "react";
import Webcam from "react-webcam";
import "./App.css"; // You may need to adjust the path

// Your sign language detection code goes here

class App extends Component {
  constructor(props) {
    super(props);
    // Initialize any state or variables here
  }

  render() {
    return (
      <div className="App">
        {/* Add your webcam component */}
        <Webcam
          audio={false}
          ref={this.webcamRef}
          width={640}
          height={480}
          screenshotFormat="image/jpeg"
        />
        {/* Add other UI components if needed */}
        <p>Output </p>
      </div>
    );
  }
}

export default App;
