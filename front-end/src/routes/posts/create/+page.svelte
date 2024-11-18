<script lang="ts">
  import { createPost, type PostParam } from '$lib/api/post';

  let post: PostParam = {
      user_id: NaN,
      post_content: '',
      post_date: '',
      likes: NaN,
      last_liked_at: '',
  };

  let message = '';

  const handleSubmit = async () => {
      try {
        post.last_liked_at =  post.last_liked_at.replace('T', ' ') + ':00';
        post.post_date =  post.post_date.replace('T', ' ') + ':00';
          const response = await createPost(post);
          if (response.status === 'success') {
              message = 'Post created successfully!';
              resetForm();
          } else {
              message = `Error: ${response.message}`;
          }
      } catch (error) {
          console.error(error);
          message = 'Error creating post.';
      }
  };

  const resetForm = () => {
      post = {
          user_id: NaN,
          post_content: '',
          post_date: '',
          likes: NaN,
          last_liked_at: '',
      };
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={post.user_id} placeholder="User ID" required />
  <textarea bind:value={post.post_content} placeholder="Post Content" required></textarea>
  <label>Post Date</label>
  <input type="datetime-local" bind:value={post.post_date} placeholder="Post Date" required />
  <input type="number" bind:value={post.likes} placeholder="Likes" />
  <label>Last Liked At</label>
  <input type="datetime-local" bind:value={post.last_liked_at} placeholder="Last Liked At" />
  <button type="submit">Create Post</button>
</form>

{#if message}
<p>{message}</p>
{/if}




<style>
*{
   margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}

/* Form Container */
form {
  max-width: 600px;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Input and Textarea Styling */
input[type="text"],
input[type="number"],
input[type="url"],
input[type="date"],
input[type="datetime-local"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #007BFF;
}

/* Button Styling */
button {
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

button:hover {
  background-color: #0056b3;
}

button:active {
  transform: scale(0.98);
}

/* Message Styling */
p {
  margin-top: 10px;
  padding: 10px;
  text-align: center;
  border-radius: 5px;
}

p.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

p.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Section for Output Display */
div {
  margin: 20px auto;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

div h2 {
  margin-bottom: 15px;
  font-size: 20px;
  color: #333;
}

div p {
  margin-bottom: 10px;
  font-size: 16px;
  color: #555;
}

div p strong {
  color: #000;
}
</style>
