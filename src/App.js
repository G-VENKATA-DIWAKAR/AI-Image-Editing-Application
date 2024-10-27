import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');
    const [enhancedImage, setEnhancedImage] = useState('');
    const [bgRemovedImage, setBgRemovedImage] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const uploadImage = async () => {
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('http://localhost:5000/upload', formData);
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Error uploading file');
        }
    };

    const enhanceImage = async () => {
        try {
            const response = await axios.post('http://localhost:5000/enhance', {
                file_path: `uploads/${file.name}`,
                brightness: 1.2,
                contrast: 1.5,
            });
            setEnhancedImage(response.data.enhanced_file_path);
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Error enhancing image');
        }
    };

    const removeBackground = async () => {
        try {
            const response = await axios.post('http://localhost:5000/remove-background', {
                file_path: `uploads/${file.name}`,
            });
            setBgRemovedImage(response.data.output_path);
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Error removing background');
        }
    };

    return (
        <div>
            <h1>AI Image Editing Application</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={uploadImage}>Upload Image</button>
            <button onClick={enhanceImage}>Enhance Image</button>
            <button onClick={removeBackground}>Remove Background</button>
            {message && <p>{message}</p>}
            {enhancedImage && <img src={`http://localhost:5000/${enhancedImage}`} alt="Enhanced" />}
            {bgRemovedImage && <img src={`http://localhost:5000/${bgRemovedImage}`} alt="Background Removed" />}
        </div>
    );
}

export default App;
