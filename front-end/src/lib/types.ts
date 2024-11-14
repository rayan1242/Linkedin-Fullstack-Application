export interface User {
  user_id: number;
  name: string;
  dob: string;
  age?: number;
  profile_pic?: string;
  location_city: string;
  location_state: string;
  location_country: string;
}

export interface Skill {
  skill_id: number;
  skill_name: string;
}

export interface Post {
  post_id: number;
  user_id: number;
  post_content: string;
  post_date: string;
  likes: number;
  last_liked_at: string;
}

export interface Job {
  job_id: number;
  institution_id: number;
  job_title: string;
  description: string;
  type: string;
}

export interface Experience {
  exp_id: number;
  user_id: number;
  institution_id: number;
  start: string;
  end: string;
  description: string;
  title: string;
  duration: number;
}

export interface Education {
  edu_id: number;
  user_id: number;
  institution_id: number;
  start: string;
  end: string;
  course: string;
  duration: number;
}

export interface Application {
  application_id: number;
  job_id: number;
  user_id: number;
  application_status: string;
  application_date: string;
}

export interface Institution {
  institution_id: number;
  no_of_employees: number;
  website: string;
  industry: string;
  name: string;
  description: string;
  location_city: string;
  location_state: string;
  location_country: string;
}
