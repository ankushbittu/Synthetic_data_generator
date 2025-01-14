import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const generateData = async (method, rows, params = {}) => {
    try {
        const response = await axios.post(`${API_URL}/generate/${method}`, {
            rows,
            params
        });
        return response.data;
    } catch (error) {
        throw error.response?.data?.error || 'An error occurred';
    }
};

export const downloadFile = (filename) => {
    window.open(`${API_URL}/static/generated_data/${filename}`);
};