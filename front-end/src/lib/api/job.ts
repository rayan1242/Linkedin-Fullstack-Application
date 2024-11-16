import axios from "axios";
import type { Job } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type JobParam = Omit<Job, "job_id">;


async function getJobs() {
  try {
    const response = await api.get("/job");
  } catch (error) {
    console.error(error);
  }
}

export async function getJob(job_id: number) {
  try {
    const response = await api.post(`/job/${job_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error getting job.' };
  }
}

export async function createJob(job: JobParam) {
  try {
    const response = await api.post("/job/create", job);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error creating job.' };
  }
}

export async function updateJob(job_id: number, job: JobParam) {
  try {
    const response = await api.put(`/job/${job_id}`, job);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error updating job.' };
  }
}

export async function deleteJob(job_id: number) {
  try {
    const response = await api.delete(`/job/${job_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error deleting job.' };
  }
}
