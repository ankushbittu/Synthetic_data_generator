import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const DataPreview = ({ previewData, method }) => {
    if (!previewData) return null;

    const ChartSection = ({ data, title }) => (
        <div className="mt-4 p-4 bg-gray-50 rounded-lg transition-all duration-300 ease-in-out">
            <h4 className="text-md font-semibold mb-2">{title}</h4>
            <div className="h-64 bg-white rounded-lg p-2">
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={Object.entries(data).map(([name, value]) => ({ name, value }))}>
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Bar dataKey="value" fill="#3B82F6" />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );

    const getCharts = () => {
        const charts = {
            'rule': [
                { data: previewData.state_distribution, title: 'State Distribution' },
                { data: previewData.age_distribution, title: 'Age Distribution' },
                { data: previewData.occupation_distribution, title: 'Occupation Distribution' }
            ],
            'statistical': [
                { data: previewData.height_distribution, title: 'Height Distribution' },
                { data: previewData.sex_distribution, title: 'Sex Distribution' }
            ],
            'agent': [
                { data: previewData.triage_distribution, title: 'Triage Level Distribution' },
                { data: previewData.disposition_distribution, title: 'Disposition Distribution' },
                { data: previewData.resource_usage, title: 'Resource Usage' }
            ],
            'model': [
                { data: previewData.hazard_distribution, title: 'Hazard Status Distribution' }
            ]
        };

        return charts[method] || [];
    };

    return (
        <div className="mt-6 p-4 border rounded-lg bg-white">
            <h3 className="text-lg font-semibold mb-4">Data Distribution Preview</h3>
            <div className="space-y-6">
                {getCharts().map((chart, index) => (
                    <ChartSection 
                        key={`${method}-${chart.title}-${index}`}
                        data={chart.data}
                        title={chart.title}
                    />
                ))}
            </div>
        </div>
    );
};

export default DataPreview;