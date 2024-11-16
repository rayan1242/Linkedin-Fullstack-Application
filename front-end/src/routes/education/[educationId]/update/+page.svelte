<script lang="ts">
  import { getEducation, updateEducation, type EducationParams } from '$lib/api/education'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let education_id: number;
  let educationData: EducationParams = {
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    course: '',
    duration:0
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

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education_id} placeholder="Education ID" required />
  <input type="number" bind:value={educationData.user_id} placeholder="User ID" required />
  <input type="number" bind:value={educationData.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={educationData.start} placeholder="Start Date" required />
  <input type="date" bind:value={educationData.end} placeholder="End Date" />
  <input type="text" bind:value={educationData.course} placeholder="Course" required />
  <input type="number" bind:value={educationData.duration} placeholder="Duration" required />
  <button type="submit">Update Education</button>
</form>

{#if message}
  <p>{message}</p>
{/if}