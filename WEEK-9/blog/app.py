from flask import Flask, render_template
print('what is happening?')
app = Flask(__name__)

data = [
    {
        "id": 1,
        "title": "Mastering Python for Data Analysis",
        "subtitle": "From Basics to Advanced Techniques",
        "category": "Data Analysis",
        "cover_image": "https://example.com/images/python-data-analysis.jpg",
        "userid": 101,
        "createdat": "2023-10-01T12:00:00Z",
        "content": "Python has become the go-to language for data analysis due to its simplicity and powerful libraries like Pandas, NumPy, and Matplotlib. In this article, we’ll explore how to use Python for data cleaning, manipulation, and visualization. We’ll also dive into advanced techniques such as time series analysis and working with large datasets using Dask. Whether you’re a beginner or an experienced analyst, this guide will help you unlock the full potential of Python for data analysis.",
        "tags": ["python", "data analysis", "pandas", "numpy", "visualization"],
        "views": 1500,
        "likes": 120,
        "comments": 45
    },
    {
        "id": 2,
        "title": "Introduction to Data Engineering with Python",
        "subtitle": "Building Robust Data Pipelines",
        "category": "Data Engineering",
        "cover_image": "https://example.com/images/data-engineering.jpg",
        "userid": 102,
        "createdat": "2023-09-25T09:30:00Z",
        "content": "Data engineering is the backbone of any data-driven organization. In this article, we’ll explore how Python can be used to build efficient and scalable data pipelines. We’ll cover tools like Apache Airflow for workflow orchestration, PySpark for big data processing, and SQLAlchemy for database interactions. You’ll also learn best practices for data validation, error handling, and monitoring. By the end of this guide, you’ll have a solid understanding of how to design and implement data pipelines using Python.",
        "tags": ["python", "data engineering", "airflow", "pyspark", "data pipelines"],
        "views": 2300,
        "likes": 300,
        "comments": 89
    },
    {
        "id": 3,
        "title": "Machine Learning with Python: A Beginner's Guide",
        "subtitle": "From Theory to Practice",
        "category": "Machine Learning",
        "cover_image": "https://example.com/images/ml-python.jpg",
        "userid": 103,
        "createdat": "2023-10-05T15:45:00Z",
        "content": "Machine learning is transforming industries, and Python is at the forefront of this revolution. In this guide, we’ll walk you through the basics of machine learning using Python’s Scikit-Learn library. We’ll cover key concepts like supervised and unsupervised learning, model evaluation, and hyperparameter tuning. You’ll also get hands-on experience by building a simple classification model. Whether you’re new to ML or looking to refresh your skills, this article will provide a strong foundation for your machine learning journey.",
        "tags": ["python", "machine learning", "scikit-learn", "AI", "data science"],
        "views": 1800,
        "likes": 250,
        "comments": 60
    },
    {
        "id": 4,
        "title": "Deep Learning with TensorFlow and Python",
        "subtitle": "Unlocking the Power of Neural Networks",
        "category": "Artificial Intelligence",
        "cover_image": "https://example.com/images/tensorflow.jpg",
        "userid": 104,
        "createdat": "2023-09-30T11:20:00Z",
        "content": "Deep learning is a subset of machine learning that focuses on neural networks. In this article, we’ll explore how to use TensorFlow, one of the most popular deep learning frameworks, with Python. We’ll cover the basics of building and training neural networks, including convolutional neural networks (CNNs) for image recognition and recurrent neural networks (RNNs) for sequence data. You’ll also learn how to use TensorFlow’s high-level API, Keras, to simplify your workflow. By the end, you’ll have the tools to start building your own deep learning models.",
        "tags": ["python", "deep learning", "tensorflow", "neural networks", "AI"],
        "views": 1200,
        "likes": 90,
        "comments": 30
    },
    {
        "id": 5,
        "title": "Data Visualization with Python",
        "subtitle": "Turning Data into Insights",
        "category": "Data Analysis",
        "cover_image": "https://example.com/images/data-visualization.jpg",
        "userid": 105,
        "createdat": "2023-10-10T08:00:00Z",
        "content": "Data visualization is a critical skill for any data professional. In this article, we’ll explore how to create stunning visualizations using Python libraries like Matplotlib, Seaborn, and Plotly. We’ll cover everything from basic charts to advanced interactive dashboards. You’ll also learn how to customize your visualizations to effectively communicate insights. Whether you’re presenting to stakeholders or exploring data for yourself, this guide will help you turn raw data into compelling stories.",
        "tags": ["python", "data visualization", "matplotlib", "seaborn", "plotly"],
        "views": 3000,
        "likes": 400,
        "comments": 120
    },
    {
        "id": 6,
        "title": "Big Data Processing with PySpark",
        "subtitle": "Scaling Data Analysis with Python",
        "category": "Data Engineering",
        "cover_image": "https://example.com/images/pyspark.jpg",
        "userid": 106,
        "createdat": "2023-10-02T14:15:00Z",
        "content": "As datasets grow larger, traditional data processing tools often fall short. PySpark, the Python API for Apache Spark, is designed to handle big data with ease. In this article, we’ll explore how to use PySpark for distributed data processing. We’ll cover key concepts like RDDs, DataFrames, and Spark SQL. You’ll also learn how to optimize your PySpark jobs for performance. Whether you’re working with terabytes of data or just getting started with big data, this guide will help you harness the power of PySpark.",
        "tags": ["python", "pyspark", "big data", "data engineering", "apache spark"],
        "views": 2100,
        "likes": 180,
        "comments": 55
    },
    {
        "id": 7,
        "title": "Natural Language Processing with Python",
        "subtitle": "Understanding Text Data",
        "category": "Artificial Intelligence",
        "cover_image": "https://example.com/images/nlp.jpg",
        "userid": 107,
        "createdat": "2023-09-28T10:10:00Z",
        "content": "Natural Language Processing (NLP) is a branch of AI that focuses on understanding and generating human language. In this article, we’ll explore how to use Python for NLP tasks like text classification, sentiment analysis, and named entity recognition. We’ll use libraries like NLTK, SpaCy, and Hugging Face Transformers. You’ll also learn how to preprocess text data and build your own NLP models. By the end, you’ll have the skills to tackle real-world NLP challenges using Python.",
        "tags": ["python", "nlp", "AI", "text analysis", "machine learning"],
        "views": 1700,
        "likes": 220,
        "comments": 70
    },
    {
        "id": 8,
        "title": "Building Machine Learning Pipelines",
        "subtitle": "From Data to Deployment",
        "category": "Machine Learning",
        "cover_image": "https://example.com/images/ml-pipelines.jpg",
        "userid": 108,
        "createdat": "2023-10-07T16:30:00Z",
        "content": "Building a machine learning model is just one part of the process. In this article, we’ll explore how to create end-to-end machine learning pipelines using Python. We’ll cover data preprocessing, feature engineering, model training, and deployment using tools like Scikit-Learn, MLflow, and FastAPI. You’ll also learn how to monitor and maintain your models in production. Whether you’re a data scientist or an engineer, this guide will help you streamline your ML workflows.",
        "tags": ["python", "machine learning", "ml pipelines", "scikit-learn", "mlflow"],
        "views": 1400,
        "likes": 150,
        "comments": 40
    },
    {
        "id": 9,
        "title": "AI in Healthcare: A Python Perspective",
        "subtitle": "Transforming Medicine with Data",
        "category": "Artificial Intelligence",
        "cover_image": "https://example.com/images/ai-healthcare.jpg",
        "userid": 109,
        "createdat": "2023-10-03T13:00:00Z",
        "content": "Artificial intelligence is revolutionizing healthcare, from diagnostics to personalized treatment plans. In this article, we’ll explore how Python is being used to build AI solutions in healthcare. We’ll cover topics like medical image analysis, predictive modeling, and natural language processing for electronic health records. You’ll also learn about the ethical considerations and challenges of deploying AI in healthcare. By the end, you’ll have a deeper understanding of how AI is transforming medicine and how you can contribute to this exciting field.",
        "tags": ["python", "AI", "healthcare", "machine learning", "data science"],
        "views": 2500,
        "likes": 280,
        "comments": 95
    },
    {
        "id": 10,
        "title": "Automating Data Workflows with Python",
        "subtitle": "Efficiency at Scale",
        "category": "Data Engineering",
        "cover_image": "https://example.com/images/automation.jpg",
        "userid": 110,
        "createdat": "2023-10-08T17:00:00Z",
        "content": "Automation is key to handling repetitive data tasks efficiently. In this article, we’ll explore how to automate data workflows using Python. We’ll cover tools like Prefect for workflow orchestration, Pandas for data manipulation, and SQLAlchemy for database interactions. You’ll also learn how to schedule and monitor automated workflows using cron jobs and logging. Whether you’re a data engineer or analyst, this guide will help you save time and reduce errors by automating your data processes.",
        "tags": ["python", "automation", "data engineering", "workflows", "data pipelines"],
        "views": 3200,
        "likes": 500,
        "comments": 150
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', data = data)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug = True)




