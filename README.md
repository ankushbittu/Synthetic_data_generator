# Synthetic Data Generator: Multi-Method Data Generation Platform

## 🎯 Why Synthetic Data?
In today's data-driven world, synthetic data is crucial for:

- Protecting privacy while maintaining data utility
- Augmenting limited datasets
- Testing software without real data 
- Training ML models when real data is scarce or sensitive
- Simulating edge cases and rare scenarios
- And also Ai workflow to train the models

Our platform tackles these challenges by providing multiple generation methods, each optimized for specific use cases.

## 🌟 Project Overview
This platform offers four distinct synthetic data generation methods, each carefully designed to produce high-quality, realistic data:

![demo image](<Screenshot 2025-01-16 132724.png>)

### Customer Profile Generation (Rule-Based)
**Why?** For testing CRM systems, marketing analyses, and user databases

**Features:**
- Interdependent attributes (age affects occupation, location affects income)
- Realistic distributions of demographics
- Geographically accurate details (state-specific phone codes, pin codes)
- Occupation-income relationships based on real-world patterns

### Physical Measurements (Statistical)
**Why?** For medical studies, anthropometric research, and product sizing

**Features:**
- Gender-specific distributions
- Correlated measurements (height affects weight)
- Realistic body measurement relationships
- Based on real-world statistical patterns

### Emergency Department Simulation (Agent-Based)
**Why?** For healthcare operations research and resource planning

**Features:**
- Realistic patient flow patterns
- Staff scheduling simulations
- Resource utilization tracking
- Multiple interlinked datasets (patients, staff, resources)
- Severity-based treatment times

### Near-Earth Object Data (CTGAN)
**Why?** For astronomical research and hazard assessment studies

**Features:**
- Complex orbital parameters
- Hazard classification
- Trained on real NEO data patterns
- Maintains complex relationships between parameters

## 🚀 Key Features

### Interactive Data Generation
- Parameter customization for each method
- Real-time generation progress tracking
- Instant data preview and visualization
- Multi-format data download options

### Data Preview & Validation
- Interactive distribution charts
- Multiple visualization types per dataset
- Real-time data quality metrics
- Cross-variable relationship visualization

## 🛠️ Technology Stack

### Frontend
- React with Vite for fast development
- Tailwind CSS for responsive design
- Recharts for interactive visualizations
- Axios for API communication

### Backend
- Flask for API endpoints
- Pandas & NumPy for data manipulation
- CTGAN for deep learning-based generation
- Mesa for agent-based simulation

### workflow
![workflow](<Untitled diagram-2025-01-15-193749.png>)

### detail info in medium page

[medium_page](https://medium.com/@ankushreddy281/building-a-synthetic-data-generator-a-multi-method-approach-with-aws-deployment-9d265c54ce94)

## 🔧 Setup & Installation

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 📊 Workflow

1. **Method Selection**
    - Choose from four generation methods
    - Each with detailed description and use cases

2. **Parameter Configuration**
    - Customize data size
    - Set method-specific parameters
    - Apply filters and constraints

3. **Data Generation**
    - Real-time progress tracking
    - Background processing for large datasets

4. **Data Preview**
    - Multiple distribution charts
    - Key statistics and metrics
    - Quality indicators

5. **Download**
    - CSV format for single datasets
    - ZIP for multiple related files
    - Consistent naming conventions

## 📂 Project Structure
```
synthetic-data-generator/
├── backend/
│   ├── app.py
│   ├── generators/
│   │   ├── rule_based.py    # Customer profiles
│   │   ├── statistical.py   # Physical measurements
│   │   ├── agent_based.py   # ED simulation
│   │   └── model_based.py   # CTGAN implementation
│   └── requirements.txt
└── frontend/
     ├── src/
     │   ├── components/      # Reusable UI components
     │   ├── services/        # API integration
     │   └── App.jsx
     └── package.json
```

## 🌟 Future Enhancements
- Additional generation methods
- More customization options
- Advanced visualization features
- API documentation
- Docker deployment support

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.Synthetic Data Generator: Multi-Method Data Generation Platform
