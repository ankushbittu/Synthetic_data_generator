import React, { useState } from 'react';
import { Database, Users, BarChart, Brain } from 'lucide-react';
import GeneratorCard from './components/GeneratorCard';
import ParameterForm from './components/ParameterForm';
import ProgressBar from './components/ProgressBar';
import DownloadSection from './components/DownloadSection';
import DataPreview from './components/DataPreview';
import { generateData, downloadFile } from './services/api';

function App() {
    const [selectedMethod, setSelectedMethod] = useState(null);
    const [rows, setRows] = useState(1000);
    const [params, setParams] = useState({});
    const [isGenerating, setIsGenerating] = useState(false);
    const [generatedFile, setGeneratedFile] = useState(null);
    const [previewData, setPreviewData] = useState(null);
    const [progress, setProgress] = useState(0);

    const methods = [
        {
            id: 'rule',
            title: 'Rule-Based',
            description: 'Generate customer profiles using predefined rules',
            icon: <Database className="w-8 h-8 mb-3 text-blue-500" />
        },
        {
            id: 'statistical',
            title: 'Statistical',
            description: 'Generate physical measurements data',
            icon: <BarChart className="w-8 h-8 mb-3 text-purple-500" />
        },
        {
            id: 'agent',
            title: 'Agent-Based',
            description: 'Generate Emergency Department simulation',
            icon: <Users className="w-8 h-8 mb-3 text-green-500" />
        },
        {
            id: 'model',
            title: 'GAN/VAE',
            description: 'Generate Near-Earth Object data',
            icon: <Brain className="w-8 h-8 mb-3 text-orange-500" />
        }
    ];

    const handleMethodSelect = (methodId) => {
        setSelectedMethod(methodId);
        // Clear previous data when switching methods
        setGeneratedFile(null);
        setPreviewData(null);
        setProgress(0);
        setParams({});
    };

    const handleGenerate = async () => {
        try {
            setIsGenerating(true);
            setProgress(0);
            setGeneratedFile(null);
            setPreviewData(null);
            
            const progressInterval = setInterval(() => {
                setProgress(prev => Math.min(prev + 10, 90));
            }, 200);
            
            const result = await generateData(selectedMethod, rows, params);
            
            clearInterval(progressInterval);
            setProgress(100);
            setGeneratedFile(result.file);
            setPreviewData(result.preview_data);
            
        } catch (error) {
            alert(error);
        } finally {
            setIsGenerating(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 p-8">
            <div className="max-w-6xl mx-auto">
                <h1 className="text-3xl font-bold mb-8 text-gray-900">
                    Synthetic Data Generator
                </h1>
                
                {/* Method Selection Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    {methods.map((method) => (
                        <GeneratorCard
                            key={method.id}
                            {...method}
                            isSelected={selectedMethod === method.id}
                            onClick={() => handleMethodSelect(method.id)}
                        />
                    ))}
                </div>

                {/* Generation Controls */}
                {selectedMethod && (
                    <div className="bg-white p-6 rounded-lg border border-gray-200">
                        <h2 className="text-xl font-semibold mb-4">
                            Configure {methods.find(m => m.id === selectedMethod)?.title}
                        </h2>
                        
                        <ParameterForm
                            method={selectedMethod}
                            params={params}
                            onParamChange={(key, value) => 
                                setParams(prev => ({ ...prev, [key]: value }))
                            }
                            rows={rows}
                            onRowsChange={setRows}
                        />

                        <div className="mt-6 space-y-4">
                            <button
                                onClick={handleGenerate}
                                disabled={isGenerating}
                                className={`
                                    px-4 py-2 rounded-md text-white font-medium
                                    ${isGenerating 
                                        ? 'bg-blue-400 cursor-not-allowed' 
                                        : 'bg-blue-600 hover:bg-blue-700'}
                                `}
                            >
                                Generate Data
                            </button>

                            {isGenerating && <ProgressBar progress={progress} />}

                            <DownloadSection
                                isGenerating={isGenerating}
                                file={generatedFile}
                                onDownload={() => downloadFile(generatedFile)}
                            />

                            {previewData && !isGenerating && (
                                <DataPreview
                                    previewData={previewData}
                                    method={selectedMethod}
                                />
                            )}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default App;