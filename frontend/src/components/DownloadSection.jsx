import React from 'react';
import { Download, Loader } from 'lucide-react';

const DownloadSection = ({ isGenerating, file, onDownload }) => {
    if (!isGenerating && !file) return null;

    return (
        <div className="mt-4 p-4 border rounded-lg bg-gray-50">
            {isGenerating ? (
                <div className="flex items-center justify-center space-x-2">
                    <Loader className="w-5 h-5 animate-spin" />
                    <span>Generating data...</span>
                </div>
            ) : file && (
                <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-600">Your data is ready!</span>
                    <button
                        onClick={onDownload}
                        className="flex items-center px-4 py-2 text-white bg-blue-600 rounded-md hover:bg-blue-700"
                    >
                        <Download className="w-4 h-4 mr-2" />
                        Download
                    </button>
                </div>
            )}
        </div>
    );
};

export default DownloadSection;