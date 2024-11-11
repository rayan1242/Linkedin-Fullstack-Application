from flask import Flask, request
from db import connect_to_database
from user import create_user, get_user, update_user, delete_user, get_all_users
from institution import create_institution, get_institution, update_institution, delete_institution, get_all_institutions
from education import create_education, get_education, update_education, delete_education, get_all_educations
from experience import create_experience, get_experience, update_experience, delete_experience, get_all_experiences
from job import create_job, get_job, update_job, delete_job, get_all_jobs
from application import create_application, get_application, update_application, delete_application, get_all_applications
from post import create_post, get_post, update_post, delete_post, get_all_posts
from skill import create_skill, get_skill, update_skill, delete_skill, get_all_skills

app = Flask(__name__)
connection = connect_to_database()

@app.route('/user/create', methods=['POST'], strict_slashes=False)
def create_user_route():
    user_data = request.json
    return create_user(user_data, connection)

@app.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user_route(user_id):
    return get_user(user_id, connection)

@app.route('/user/update/<int:user_id>', methods=['PUT'], strict_slashes=False)
def update_user_route(user_id):
    user_data = request.json
    return update_user(user_id, user_data, connection)

@app.route('/user/delete/<int:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_route(user_id):
    return delete_user(user_id, connection)

@app.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users_route():
    return get_all_users(connection)

@app.route('/institution/create', methods=['POST'], strict_slashes=False)
def create_institution_route():
    institution_data = request.json
    return create_institution(institution_data, connection)

@app.route('/institution/<int:institution_id>', methods=['GET'], strict_slashes=False)
def get_institution_route(institution_id):
    return get_institution(institution_id, connection)

@app.route('/institution/update/<int:institution_id>', methods=['PUT'], strict_slashes=False)
def update_institution_route(institution_id):
    institution_data = request.json
    return update_institution(institution_id, institution_data, connection)

@app.route('/institution/delete/<int:institution_id>', methods=['DELETE'], strict_slashes=False)
def delete_institution_route(institution_id):
    return delete_institution(institution_id, connection)

@app.route('/institutions', methods=['GET'], strict_slashes=False)
def get_all_institutions_route():
    return get_all_institutions(connection)

@app.route('/education/create', methods=['POST'], strict_slashes=False)
def create_education_route():
    education_data = request.json
    return create_education(education_data, connection)

@app.route('/education/<int:education_id>', methods=['GET'], strict_slashes=False)
def get_education_route(education_id):
    return get_education(education_id, connection)

@app.route('/education/update/<int:education_id>', methods=['PUT'], strict_slashes=False)
def update_education_route(education_id):
    education_data = request.json
    return update_education(education_id, education_data, connection)

@app.route('/education/delete/<int:education_id>', methods=['DELETE'], strict_slashes=False)
def delete_education_route(education_id):
    return delete_education(education_id, connection)

@app.route('/educations', methods=['GET'], strict_slashes=False)
def get_all_educations_route():
    return get_all_educations(connection)

@app.route('/experience/create', methods=['POST'], strict_slashes=False)
def create_experience_route():
    experience_data = request.json
    return create_experience(experience_data, connection)

@app.route('/experience/<int:experience_id>', methods=['GET'], strict_slashes=False)
def get_experience_route(experience_id):
    return get_experience(experience_id, connection)

@app.route('/experience/update/<int:experience_id>', methods=['PUT'], strict_slashes=False)
def update_experience_route(experience_id):
    experience_data = request.json
    return update_experience(experience_id, experience_data, connection)

@app.route('/experience/delete/<int:experience_id>', methods=['DELETE'], strict_slashes=False)
def delete_experience_route(experience_id):
    return delete_experience(experience_id, connection)

@app.route('/experiences', methods=['GET'], strict_slashes=False)
def get_all_experiences_route():
    return get_all_experiences(connection)

@app.route('/job/create', methods=['POST'], strict_slashes=False)
def create_job_route():
    job_data = request.json
    return create_job(job_data, connection)

@app.route('/job/<int:job_id>', methods=['GET'], strict_slashes=False)
def get_job_route(job_id):
    return get_job(job_id, connection)

@app.route('/job/update/<int:job_id>', methods=['PUT'], strict_slashes=False)
def update_job_route(job_id):
    job_data = request.json
    return update_job(job_id, job_data, connection)

@app.route('/job/delete/<int:job_id>', methods=['DELETE'], strict_slashes=False)
def delete_job_route(job_id):
    return delete_job(job_id, connection)

@app.route('/jobs', methods=['GET'], strict_slashes=False)
def get_all_jobs_route():
    return get_all_jobs(connection)

@app.route('/application/create', methods=['POST'], strict_slashes=False)
def create_application_route():
    application_data = request.json
    return create_application(application_data, connection)

@app.route('/application/<int:application_id>', methods=['GET'], strict_slashes=False)
def get_application_route(application_id):
    return get_application(application_id, connection)

@app.route('/application/update/<int:application_id>', methods=['PUT'], strict_slashes=False)
def update_application_route(application_id):
    application_data = request.json
    return update_application(application_id, application_data, connection)

@app.route('/application/delete/<int:application_id>', methods=['DELETE'], strict_slashes=False)
def delete_application_route(application_id):
    return delete_application(application_id, connection)

@app.route('/applications', methods=['GET'], strict_slashes=False)
def get_all_applications_route():
    return get_all_applications(connection)

@app.route('/post/create', methods=['POST'], strict_slashes=False)
def create_post_route():
    post_data = request.json
    return create_post(post_data, connection)

@app.route('/post/<int:post_id>', methods=['GET'], strict_slashes=False)
def get_post_route(post_id):
    return get_post(post_id, connection)

@app.route('/post/update/<int:post_id>', methods=['PUT'], strict_slashes=False)
def update_post_route(post_id):
    post_data = request.json
    return update_post(post_id, post_data, connection)

@app.route('/post/delete/<int:post_id>', methods=['DELETE'], strict_slashes=False)
def delete_post_route(post_id):
    return delete_post(post_id, connection)

@app.route('/posts', methods=['GET'], strict_slashes=False)
def get_all_posts_route():
    return get_all_posts(connection)

@app.route('/skill/create', methods=['POST'], strict_slashes=False)
def create_skill_route():
    skill_data = request.json
    return create_skill(skill_data, connection)

@app.route('/skill/<int:skill_id>', methods=['GET'], strict_slashes=False)
def get_skill_route(skill_id):
    return get_skill(skill_id, connection)

@app.route('/skill/update/<int:skill_id>', methods=['PUT'], strict_slashes=False)
def update_skill_route(skill_id):
    skill_data = request.json
    return update_skill(skill_id, skill_data, connection)

@app.route('/skill/delete/<int:skill_id>', methods=['DELETE'], strict_slashes=False)
def delete_skill_route(skill_id):
    return delete_skill(skill_id, connection)

@app.route('/skills', methods=['GET'], strict_slashes=False)
def get_all_skills_route():
    return get_all_skills(connection)

if __name__ == '__main__':
    app.run(debug=True, port=3000)