<script lang="ts">
  import { getSkill } from '$lib/api/skill';

  let skill_id: number;
  let skill = { skill_id: 0, skill_name: '' };
  let message = '';

  const handleSubmit = async () => {
      try {
          const response = await getSkill(String(skill_id));
          if (response.status === 'success') {
              skill = response.skill;
              message = '';
          } else {
              skill = { skill_id: 0, skill_name: '' };
              message = `Error: ${response.message}`;
          }
      } catch (error) {
          console.error(error);
          message = 'Error fetching skill.';
      }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={skill_id} placeholder="Skill ID" required />
  <button type="submit">Get Skill</button>
</form>

{#if message}
  <p class="error">{message}</p>
{/if}

{#if skill.skill_id}
  <div>
      <h2>Skill Details</h2>
      <p><strong>ID:</strong> {skill.skill_id}</p>
      <p><strong>Name:</strong> {skill.skill_name}</p>
  </div>
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
  margin: 20% auto;
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
