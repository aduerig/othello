#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
#include <vector>
#include "engine.hpp"
#include "player.hpp"



#include "engine.hpp"
#include <iostream>
#include <chrono>
#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>

#include <errno.h> 
#include <unistd.h> 
#include <string.h>
#include <time.h>
#include <semaphore.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdarg.h>
#include <cstdio>
#include <stdlib.h>
#include <string>
#include <inttypes.h>
#include <unistd.h>


struct new_params
{
    int size;
    std::string semaphore_name;
    std::string shared_memory_name;
    int permissions;
};

class Driver
{
    public:
        Driver();
        void run_driver(int games_to_play, int iterations_per_move, std::string model_name, bool print_on, int depth);
    private:
    	std::string get_newest_model_name();
        int play_game(Engine* e, std::vector<Player*> players, int* num_moves, bool print_on);
        void call_python_script_helper(new_params params, std::string model_name);
        int setup_python_communication();
        void send_end_code_python();
        int destroy_communication();
        std::string gen_random(const int len);
        void cleanup();
        void read_game_info(std::string game_path, int *n_moves, U64 *player_boards, U64 *opponent_boards, float **MCvals, int *result, float *saved_values);
        int acquire_semaphore(sem_t *pSemaphore);
        int release_semaphore(sem_t *pSemaphore); 

        // communication variables
        sem_t *pSemaphore;
        int rc;
        void *pSharedMemory_code;
        void *pSharedMemory_rest;
        int fd;
        struct new_params params;

        // sender flag
        int32_t send_code; // -1 is nothing, 0 is c sent, 1 is python sent
};
