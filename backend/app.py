from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
from generators.rule_based import RuleBasedGenerator
from generators.statistical import StatisticalGenerator
from generators.agent_based import AgentBasedGenerator
from generators.model_based import ModelBasedGenerator
import os
import pandas as pd
from zipfile import ZipFile
import shutil


app = Flask(__name__)
CORS(app)

# Ensure generated_data directory exists
os.makedirs('static/generated_data', exist_ok=True)

# Initialize generators
rule_generator = RuleBasedGenerator()
statistical_generator = StatisticalGenerator()
agent_generator = AgentBasedGenerator()
model_generator = ModelBasedGenerator()

@app.route('/generate/<method>', methods=['POST'])
def generate_data(method):
    try:
        data = request.get_json()
        rows = data.get('rows', 1000)
        params = data.get('params', {})
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        if method == 'rule':
            df = rule_generator.generate_data(rows, params)
            filename = f"rule_based_{timestamp}.csv"
            filepath = os.path.join('static/generated_data', filename)
            df.to_csv(filepath, index=False)
            
            # Create preview data
            preview_data = {
                'state_distribution': df['state'].value_counts().to_dict(),
                'age_distribution': df['age'].value_counts().to_dict(),
                'occupation_distribution': df['occupation'].value_counts().to_dict()
            }
            
            return jsonify({
                'status': 'success',
                'file': filename,
                'preview_data': preview_data,
                'rows': rows
            })

        elif method == 'statistical':
            df = statistical_generator.generate_data(rows, params)
            filename = f"statistical_{timestamp}.csv"
            filepath = os.path.join('static/generated_data', filename)
            df.to_csv(filepath, index=False)
            
            # Create height ranges for preview
            df['height_range'] = pd.cut(df['height'], bins=10).astype(str)
            preview_data = {
                'height_distribution': df['height_range'].value_counts().to_dict(),
                'sex_distribution': df['sex'].value_counts().to_dict()
            }
            
            return jsonify({
                'status': 'success',
                'file': filename,
                'preview_data': preview_data,
                'rows': rows
            })

        elif method == 'agent':
            df_patients, df_staff, df_resources = agent_generator.generate_data(rows, params)
            
            # Create preview data
            preview_data = {
                'triage_distribution': df_patients['triage_level'].value_counts().to_dict(),
                'disposition_distribution': df_patients['disposition'].value_counts().to_dict(),
                'resource_usage': df_resources['resource_id'].value_counts().to_dict()
            }
            
            # Save files
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            files = {
                'patients': f"ed_patients_{timestamp}.csv",
                'staff': f"ed_staff_{timestamp}.csv",
                'resources': f"ed_resources_{timestamp}.csv"
            }
            
            zip_filename = f'ed_simulation_{timestamp}.zip'
            zip_filepath = os.path.join('static/generated_data', zip_filename)
            
            with ZipFile(zip_filepath, 'w') as zipf:
                for key, filename in files.items():
                    filepath = os.path.join('static/generated_data', filename)
                    if key == 'patients':
                        df_patients.to_csv(filepath, index=False)
                    elif key == 'staff':
                        df_staff.to_csv(filepath, index=False)
                    else:
                        df_resources.to_csv(filepath, index=False)
                    zipf.write(filepath, filename)
                    os.remove(filepath)
            
            return jsonify({
                'status': 'success',
                'file': zip_filename,
                'preview_data': preview_data,
                'rows': rows
            })

        elif method == 'model':
            df = model_generator.generate_data(rows, params)
            filename = f"neo_data_{timestamp}.csv"
            filepath = os.path.join('static/generated_data', filename)
            df.to_csv(filepath, index=False)
            
            preview_data = {
                'hazard_distribution': df['Hazardous'].value_counts().to_dict()
            }
            
            return jsonify({
                'status': 'success',
                'file': filename,
                'preview_data': preview_data,
                'rows': rows
            })

        else:
            return jsonify({'error': 'Invalid method'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(
            os.path.join('static/generated_data', filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)