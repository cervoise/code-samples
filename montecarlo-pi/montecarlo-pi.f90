program fortran
   implicit none
   integer :: z
   integer :: N
   real :: pi
   real :: x
   real :: y
   integer :: i
   
   N = 10000000
   z = 0

   do i=1,N
      x = rand()
	  y = rand()
      if (x**2+y**2 < 1) then
         z = z+1
      end if
   end do

   pi = 4*REAL(z)/REAL(N)

   print *, 'Estimation de pi:  ',pi
end program fortran