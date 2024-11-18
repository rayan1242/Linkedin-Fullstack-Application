import axios from "axios";
import type { Job } from "$lib/types";

export type JobParam = Omit<Job, "job_id">;

export async function getJobs() {
  const response = await axios.get("http://localhost:3000/job");
  return response.data;
}

export async function getJob(job_id: string) {
  const response = await axios.get(`http://localhost:3000/job/${job_id}`);
  return response.data;
}

export async function createJob(job: JobParam) {
  const response = await axios.post("http://localhost:3000/job/create", job);
  return response.data;
}

export async function updateJob(job_id: string, job: JobParam) {
  const response = await axios.put(`http://localhost:3000/job/${job_id}`, job);
  return response.data;
}

export async function deleteJob(job_id: string) {
  const response = await axios.delete(`http://localhost:3000/job/${job_id}`);
  return response.data;
}
