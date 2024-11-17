import axios from "axios";
import type { Post } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type PostParam = Omit<Post, "post_id">;

async function getPosts() {
  try {
    const response = await api.get("/post");
  } catch (error) {
    console.error(error);
  }
}

export async function getPost(post_id: number) {
  try {
    const response = await api.post(`/post/${post_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return  { status: 'error', message: 'Error getting post.' };
  }
}

export async function createPost(post: PostParam) {
  try {
    const response = await api.post("/post/create", post);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error creating post.' };
  }

}

export async function updatePost(post_id: number, post: PostParam) {
  try {
    const response = await api.put(`/post/${post_id}`, post);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error updating post.' };
  }
}

export async function deletePost(post_id: number) {
  try {
    const response = await api.delete(`/post/${post_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error deleting post.' };
  }
}
