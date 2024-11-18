<script lang="ts">
  import { getExperience } from '$lib/api/experience'; // Adjust the import path as necessary

  let exp_id: string;
  let message = '';
  let experience = { 
    exp_id: '',
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    description: '',
    title: '',
    duration: 0
  };

  const handleSubmit = async () => {
      const response = await getExperience(exp_id);
      if (response.status === 'success'){ 
        experience = response.experience;
        message = '';
      }
       else {
        message = `Error: ${response.message}`;
        experience = {
          exp_id: '',
          user_id: 0,
          institution_id: 0,
          start: '',
          end: '',
          description: '',
          title: '',
          duration: 0
        };
      }
};
</script>

<style>
  form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20% auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input, button {
    margin-bottom: 1rem;
    padding: 0.5rem;
    font-size: 1rem;
  }

  button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    color: red;
  }

  .experience-details {
    max-width: 400px;
    margin: 1rem auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={exp_id} placeholder="Experience ID" required />
  <button type="submit">Get Experience</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

{#if experience.exp_id}
  <div class="experience-details">
    <h2>Experience Details</h2>
    <p><strong>ID:</strong> {experience.exp_id}</p>
    <p><strong>User ID:</strong> {experience.user_id}</p>
    <p><strong>Institution ID:</strong> {experience.institution_id}</p>
    <p><strong>Start Date:</strong> {experience.start}</p>
    <p><strong>End Date:</strong> {experience.end}</p>
    <p><strong>Description:</strong> {experience.description}</p>
    <p><strong>Title:</strong> {experience.title}</p>
    <p><strong>Duration:</strong> {experience.duration}</p>
  </div>
{/if}