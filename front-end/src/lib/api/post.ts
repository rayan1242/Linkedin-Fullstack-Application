import axios from "axios";
import type { Post } from "$lib/types";

export type PostParam = Omit<Post, "post_id">;

export async function getPosts() {
  const response = await axios.get("http://localhost:3000/post");
  return response.data;
}

export async function getPost(post_id: string) {
  const response = await axios.get(`http://localhost:3000/post/${post_id}`);
  return response.data;
}

export async function createPost(post: PostParam) {
  const response = await axios.post("http://localhost:3000/post/create", post);
  return response.data;
}

export async function updatePost(post_id: string, post: PostParam) {
  const response = await axios.put(
    `http://localhost:3000/post/${post_id}`,
    post
  );
  return response.data;
}

export async function deletePost(post_id: string) {
  const response = await axios.delete(`http://localhost:3000/post/${post_id}`);
  return response.data;
}
