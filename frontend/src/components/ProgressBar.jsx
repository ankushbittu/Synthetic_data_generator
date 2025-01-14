// components/ProgressBar.jsx
import React from 'react';

const ProgressBar = ({ progress }) => {
    return (
        <div className="w-full bg-gray-200 rounded-full h-2.5">
            <div 
                className="bg-blue-600 h-2.5 rounded-full transition-all duration-500"
                style={{ width: `${progress}%` }}
            />
        </div>
    );
};

export default ProgressBar;