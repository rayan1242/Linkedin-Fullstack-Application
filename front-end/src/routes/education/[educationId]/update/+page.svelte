<script lang="ts">
  import { getEducation, updateEducation, type EducationParam } from '$lib/api/education'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let education_id: string;
  let educationData: EducationParam = {
    user_id:0,
    institution_id:0,
    start: '',
    end: '',
    course: '',
  };

  let message = '';

  onMount(async () => {
    try {
      const education = await getEducation(education_id);
      educationData = education;
    } catch (e: any) {
      console.log(e);
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await updateEducation(education_id, educationData);
      if (response.status === 'success') {
        message = 'Education record updated successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error updating education record.';
    }
  };
</script>

<style>
  form {
    max-width: 600px;
    margin: 0 auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input, button {
    display: block;
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  input:focus {
    border-color: #007BFF;
    outline: none;
  }

  button {
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    text-align: center;
    color: green;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education_id} placeholder="Education ID" required />
  <input type="number" bind:value={educationData.user_id} placeholder="User ID" required />
  <input type="number" bind:value={educationData.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={educationData.start} placeholder="Start Date" required />
  <input type="date" bind:value={educationData.end} placeholder="End Date" />
  <input type="text" bind:value={educationData.course} placeholder="Course" required />
  <button type="submit">Update Education</button>
</form>

{#if message}
  <p>{message}</p>
{/if}