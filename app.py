from flask import Flask, render_template

app = Flask(__name__)

# Replace this with your actual degree scores data
degree_data = {
    'Semester 1': [
        {'course': 'Physics Laboratory A1', 'score': 89, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Classical Physics 1', 'score': 67, 'weight': 6, 'taken': False, 'marked': False},
        {'course': 'Introductory Mathematics for Physicists1', 'score': 91, 'weight': 6, 'taken': True, 'marked': False},
        {'course': 'Calculus 1a for Physicists', 'score': 60, 'weight': 7, 'taken': False, 'marked': False},
        {'course': 'Linear Algebra for Electrical Engineering', 'score': 88, 'weight': 6, 'taken': True, 'marked': False},
    ],
    'Semester 2': [
        {'course': 'Introduction to Thermodynamics and States of Matter', 'score': 61, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Physics Laboratory A2', 'score': 87, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Classical Physics 2', 'score': 97, 'weight': 6, 'taken': False, 'marked': False},
        {'course': 'Special Relativity', 'score': 68, 'weight': 2, 'taken': True, 'marked': False},
        {'course': 'Introductory Mathematics for Physicists 2', 'score': 72, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Programming - Python', 'score': 97, 'weight': 3, 'taken': False, 'marked': False},
        {'course': 'Digital Logic Systems', 'score': 82, 'weight': 3.5, 'taken': False, 'marked': False},
    ],
    'Semester 3': [
        {'course': 'Analytical Mechanics', 'score': 98, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Physics Laboratory B1', 'score': 99, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Methods of Theoretical Physics 1', 'score': 64, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Intr. to Probability and Statistics', 'score': 84, 'weight': 3.5, 'taken': True, 'marked': False},
        {'course': 'Introduction to Devices', 'score': 85, 'weight': 2.5, 'taken': True, 'marked': False},
        {'course': 'Linear Circuits and Systems', 'score': 82, 'weight': 5, 'taken': True, 'marked': False},
    ],
    'Semester 4': [
        {'course': 'Thermal Physics', 'score': 74, 'weight': 5, 'taken': True, 'marked': False},
        {'course': 'Physics Laboratory B2', 'score': 97, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Quantum Theory 1', 'score': 68, 'weight': 5, 'taken': True, 'marked': False},
        {'course': 'Electronic Devices', 'score': 65, 'weight': 5.5, 'taken': True, 'marked': False},
        {'course': 'Electromagnetic Fields', 'score': 79, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Signals and Systems', 'score': 74, 'weight': 4, 'taken': True, 'marked': False},
    ],
    'Semester 5': [
        {'course': 'Data Structures and Algorithms', 'score': 78, 'weight': 0, 'taken': True, 'marked': False},
        {'course': 'Analog Electronic Circuits', 'score': 84, 'weight': 5.5, 'taken': True, 'marked': False},
        {'course': 'Wave Transmission and Distributed Systems', 'score': 71, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Introduction to Control Theory', 'score': 90, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Electronics - Laboratory (1)', 'score': 95, 'weight': 2, 'taken': True, 'marked': False},
        {'course': 'Double Stars and Planets', 'score': 88, 'weight': 3, 'taken': True, 'marked': False},
    ],
    'Semester 6': [
        {'course': 'Methods of Theoretical Physics 2', 'score': 67, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Physics Laboratory C-sem. B', 'score': 96, 'weight': 9, 'taken': True, 'marked': False},
        {'course': 'Introduction to physical chemistry for physicists', 'score': 92, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Digital Electronic Circuits', 'score': 69, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Electronics - Laboratory (2)', 'score': 84, 'weight': 2, 'taken': True, 'marked': False},
        {'course': 'Microwave Engineering', 'score': 74, 'weight': 4, 'taken': True, 'marked': False},
    ],
    'Semester 7': [
        {'course': 'Quantum Theory 2', 'score': 69, 'weight': 6, 'taken': True, 'marked': False},
        {'course': 'Introduction to Solid State Physics', 'score': 75, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Programming 2 - C', 'score': 85, 'weight': 3.5, 'taken': True, 'marked': False},
        {'course': 'Electronics - Laboratory (3)', 'score': 75, 'weight': 2, 'taken': True, 'marked': False},
        {'course': 'Project', 'score': 91, 'weight': 6, 'taken': True, 'marked': False},
        {'course': 'Passive Microwave Devices', 'score': 100, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Space-systems Engineering', 'score': 96, 'weight': 4, 'taken': True, 'marked': False},
    ],
    'Semester 8': [
        {'course': 'Introduction to Particles and Nuclei', 'score': 86, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Numerical Analysis', 'score': 92, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Spectral Methods for Wavefields Excitation and Radiation', 'score': 75, 'weight': 3, 'taken': True, 'marked': False},
        {'course': 'Random Signals and Noise', 'score': 73, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Practical Feedback Systems', 'score': 91, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'A C Languague Workshop', 'score': 91, 'weight': 2, 'taken': True, 'marked': False},
        {'course': 'Introduction to opto-electronic devices', 'score': 89, 'weight': 4, 'taken': True, 'marked': False},
        {'course': 'Advanced Laboratory for Microwaves', 'score': 100, 'weight': 1.5, 'taken': True, 'marked': False},
    ],
}
@app.route('/')
def index():
    return render_template('index', degree_data=degree_data)

@app.route('/Record_of_studies')
def record_of_studies():
    return render_template('record_of_studies', degree_data=degree_data)

@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)
