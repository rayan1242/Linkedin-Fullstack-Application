import axios from "axios";
import type { Post } from "$lib/types";

async function getPosts() {
  try {
    const response = await axios.get("/post");
  } catch (error) {
    console.error(error);
  }
}

async function getPost(post_id: string) {
  try {
    const response = await axios.post(`/post/${post_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createPost(post: Post) {
  try {
    const response = await axios.post("/post/create", post);
  } catch (error) {
    console.error(error);
  }
}

async function updatePost(post_id: string, post: Post) {
  try {
    const response = await axios.put(`/post/${post_id}`, post);
  } catch (error) {
    console.error(error);
  }
}

async function deletePost(post_id: string) {
  try {
    const response = await axios.delete(`/post/${post_id}`);
  } catch (error) {
    console.error(error);
  }
}
