import axios from "axios";
import type { User } from "$lib/types";

async function getUsers() {
  try {
    const response = await axios.get("/user");
  } catch (error) {
    console.error(error);
  }
}

async function getUser(user_id: string) {
  try {
    const response = await axios.post(`/user/${user_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createUser(user: User) {
  try {
    const response = await axios.post("/user/create", user);
  } catch (error) {
    console.error(error);
  }
}

async function updateUser(user_id: string, user: User) {
  try {
    const response = await axios.put(`/user/${user_id}`, user);
  } catch (error) {
    console.error(error);
  }
}

async function deleteUser(user_id: string) {
  try {
    const response = await axios.delete(`/user/${user_id}`);
  } catch (error) {
    console.error(error);
  }
}
