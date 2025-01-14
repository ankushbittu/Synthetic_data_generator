import React from 'react';
import { Database, Users, ChartBar, Brain } from 'lucide-react';

const GeneratorCard = ({ title, description, isSelected, onClick }) => {
    const getIcon = (title) => {
        switch (title) {
            case 'Rule-Based':
                return <Database className="w-8 h-8 mb-3 text-blue-500" />;
            case 'Agent-Based':
                return <Users className="w-8 h-8 mb-3 text-green-500" />;
            case 'Statistical':
                return <ChartBar className="w-8 h-8 mb-3 text-purple-500" />;
            case 'GAN/VAE':
                return <Brain className="w-8 h-8 mb-3 text-orange-500" />;
            default:
                return null;
        }
    };

    return (
        <div
            onClick={onClick}
            className={`
                p-6 rounded-lg cursor-pointer transition-all
                ${isSelected 
                    ? 'bg-blue-100 border-2 border-blue-500' 
                    : 'bg-white border border-gray-200 hover:border-blue-300'}
            `}
        >
            {getIcon(title)}
            <h3 className="text-lg font-semibold mb-2">{title}</h3>
            <p className="text-sm text-gray-600">{description}</p>
        </div>
    );
};

export default GeneratorCard;