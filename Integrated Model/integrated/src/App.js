import React, { useState } from "react";
import "./App.css";
import useClipboard from "react-use-clipboard";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";
import Webcam from "react-webcam";

const App = () => {
  const [textToCopy, setTextToCopy] = useState("");
  const [isCopied, setCopied] = useClipboard(textToCopy, {
    successDuration: 1000,
  });

  const startListening = () =>
    SpeechRecognition.startListening({ continuous: true, language: "en-IN" });
  const { transcript, browserSupportsSpeechRecognition } =
    useSpeechRecognition();

  const webcamRef = React.useRef(null);

  if (!browserSupportsSpeechRecognition) {
    return null;
  }

  return (
    <div className="container">
      <h2>Transcription & Sign Detection</h2>
      <div className="main-content" onClick={() => setTextToCopy(transcript)}>
        {transcript}
      </div>

      <div className="btn-style">
        <button onClick={setCopied}>
          {isCopied ? "Copied!" : "Copy to clipboard"}
        </button>
        <button onClick={startListening}>Start Listening</button>
        <button onClick={SpeechRecognition.stopListening}>
          Stop Listening!
        </button>
      </div>

      {/* Webcam component */}
      <div className="webcam-container">
        <Webcam
          audio={false}
          ref={webcamRef}
          width={720}
          height={560}
          screenshotFormat="image/jpeg"
        />
      </div>
      <div className="btn-style">
        {/* Add functionality to flip Camera */}
        <camflip onClick={startListening}>Front Camera</camflip>
        <camflip onClick={SpeechRecognition.stopListening}>Back Camera</camflip>
      </div>
    </div>
  );
};

export default App;
