<script lang="ts">
  import { getExperience } from '$lib/api/experience'; // Adjust the import path as necessary

  let experience_id: number;
  let message = '';
  let experience = {
    exp_id: 0,
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    description: '',
    title: '',
    duration: 0
  };

  const handleSubmit = async () => {
    try {
      const response = await getExperience(experience_id);
      if (response.status === 'success') {
        experience = response.experience;
        message = '';
      } else {
        message = `Error: ${response.message}`;
        experience = {
          exp_id: 0,
          user_id: 0,
          institution_id: 0,
          start: '',
          end: '',
          description: '',
          title: '',
          duration: 0
        };
      }
    } catch (error) {
      console.error(error);
      message = 'Error fetching experience record.';
      experience = {
        exp_id: 0,
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

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={experience_id} placeholder="Experience ID" required />
  <button type="submit">Get Experience</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

{#if experience.exp_id}
  <div>
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