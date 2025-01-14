import React from 'react';

const ParameterForm = ({ method, params, onParamChange, rows, onRowsChange }) => {
    const getParameterInputs = () => {
        switch (method) {
            case 'rule':
                return (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700">State Filter</label>
                            <select 
                                className="mt-1 block w-full p-2 border rounded-md"
                                onChange={(e) => onParamChange('state', e.target.value)}
                            >
                                <option value="">All States</option>
                                <option value="CA">California</option>
                                <option value="NY">New York</option>
                                <option value="TX">Texas</option>
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Age Range</label>
                            <div className="flex gap-2">
                                <input 
                                    type="number" 
                                    placeholder="Min"
                                    className="mt-1 block w-full p-2 border rounded-md"
                                    onChange={(e) => onParamChange('ageMin', e.target.value)}
                                />
                                <input 
                                    type="number" 
                                    placeholder="Max"
                                    className="mt-1 block w-full p-2 border rounded-md"
                                    onChange={(e) => onParamChange('ageMax', e.target.value)}
                                />
                            </div>
                        </div>
                    </div>
                );
            
            case 'agent':
                return (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Staff Count</label>
                            <input 
                                type="number" 
                                className="mt-1 block w-full p-2 border rounded-md"
                                defaultValue={10}
                                onChange={(e) => onParamChange('staffCount', e.target.value)}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Simulation Days</label>
                            <input 
                                type="number" 
                                className="mt-1 block w-full p-2 border rounded-md"
                                defaultValue={7}
                                onChange={(e) => onParamChange('days', e.target.value)}
                            />
                        </div>
                    </div>
                );

            case 'statistical':
                return null; // No additional parameters needed

            case 'model':
                return (
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Object Type</label>
                        <select 
                            className="mt-1 block w-full p-2 border rounded-md"
                            onChange={(e) => onParamChange('objectType', e.target.value)}
                        >
                            <option value="all">All Types</option>
                            <option value="hazardous">Hazardous Only</option>
                            <option value="non-hazardous">Non-Hazardous Only</option>
                        </select>
                    </div>
                );

            default:
                return null;
        }
    };

    return (
        <div className="space-y-4">
            <div>
                <label className="block text-sm font-medium text-gray-700">
                    Number of Records
                </label>
                <input
                    type="number"
                    value={rows}
                    onChange={(e) => onRowsChange(e.target.value)}
                    className="mt-1 block w-full p-2 border rounded-md"
                    min="1"
                />
            </div>
            {getParameterInputs()}
        </div>
    );
};

export default ParameterForm;